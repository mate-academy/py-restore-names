import pytest
from typing import Generator
from app.restore_names import restore_names


@pytest.fixture()
def users_list() -> Generator:
    yield [
        {"first_name": None, "full_name": "Ray Leonard"},
        {"full_name": "Ray Leonard"},
    ]


def test_first_name_in_users_list(users_list: list[dict]) -> None:
    restore_names(users_list)
    assert users_list[0]["first_name"] == "Ray"
    assert users_list[1]["first_name"] == "Ray"
