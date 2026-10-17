"""Слой окружений — по образцу auto_tests_vshgu/config/environments.py, в
минимальном виде: один стенд (develop), логин/пароль из .env."""
from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")


@dataclass(frozen=True)
class Environment:
    name: str
    base_url: str
    login: str
    password: str


ENVIRONMENTS = {
    "develop": Environment(
        name="develop",
        base_url=os.getenv("DEVELOP_URL", "https://develop-experts.d4.devspark.ru").rstrip("/"),
        login=os.getenv("DEVELOP_LOGIN", ""),
        password=os.getenv("DEVELOP_PASSWORD", ""),
    ),
}
