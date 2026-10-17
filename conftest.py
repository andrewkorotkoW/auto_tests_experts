"""Корневой conftest — по образцу auto_tests_vshgu: --env выбирает стенд из
config.environments.ENVIRONMENTS, admin_session логинится в админку (Laravel
Backpack: GET /admin/login за CSRF-токеном из скрытого поля формы, POST
/admin/login формой — подтверждено разведкой 17.10.2026, см.
docs/recon_2026-10-17.md)."""
import re

import pytest
import requests

from config.environments import ENVIRONMENTS


def pytest_addoption(parser):
    parser.addoption("--env", default="develop", choices=sorted(ENVIRONMENTS))


@pytest.fixture(scope="session")
def env(request):
    return ENVIRONMENTS[request.config.getoption("--env")]


@pytest.fixture
def admin_session(env):
    session = requests.Session()
    login_page = session.get(f"{env.base_url}/admin/login", timeout=30)
    match = re.search(r'name="_token" value="([^"]+)"', login_page.text)
    assert match, f"Не найден CSRF-токен на странице логина {env.base_url}/admin/login"

    resp = session.post(
        f"{env.base_url}/admin/login",
        data={"_token": match.group(1), "email": env.login, "password": env.password},
        headers={"Referer": f"{env.base_url}/admin/login"},
        timeout=30,
    )
    assert resp.status_code in (200, 302), f"Логин не удался: HTTP {resp.status_code}"
    return session
