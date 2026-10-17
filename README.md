# auto_tests_experts

Автотесты АИС «Эксперт» (develop-experts.d4.devspark.ru) — система учёта
экспертов-докладчиков образовательных проектов Президентской академии.

Минимальный скелет (17.10.2026) — по образцу auto_tests_vshgu, сильно упрощён:
один стенд (`develop`), сессионный логин в админку (Laravel Backpack CRUD).

## Запуск

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
cp .env.example .env   # вписать DEVELOP_LOGIN/DEVELOP_PASSWORD
.venv/bin/python -m pytest -v
```

## Структура

- `config/environments.py` — стенды, читает `.env`
- `conftest.py` — `--env`, фикстуры `env`/`admin_session`
- `tests/api/...` — API-тесты (по областям админки)

## Разделы админки (разведка 17.10.2026)

Laravel Backpack CRUD, `/admin/{resource}` + `POST /admin/{resource}/search`
(server-side DataTables): project, program, organizations, positions,
broad-topics, detailed-topics, regions, city, places-work, education,
additional-education, education-program, education-level, university,
academic-title, academic-degree, list-achievement, expert-work-project,
expert-work-program, telegram-settings; ролевая модель — users, roles,
permission, role-permission-management, security/monitor,
security/suspicious-activities. Публичный каталог — `/experts`.
