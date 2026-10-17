import pytest


@pytest.mark.api
@pytest.mark.smoke
class TestLoginApi:
    def test_admin_login_succeeds(self, admin_session, env):
        resp = admin_session.get(f"{env.base_url}/admin/dashboard", timeout=30)
        assert resp.status_code == 200
        assert "login-form" not in resp.text, "Вернулась форма логина — сессия не авторизована"

    def test_anon_dashboard_redirects_to_login(self, env):
        import requests
        resp = requests.get(f"{env.base_url}/admin/dashboard", timeout=30, allow_redirects=True)
        assert "/admin/login" in resp.url
