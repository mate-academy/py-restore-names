from collections.abc import Generator
from typing import Any

import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_list() -> Generator[list[dict], Any, Any]:
    yield [
        {"first_name": None, "full_name": "Mark Black"},
        {"full_name": "Mark Black"},
    ]


def test_first_name_is_none(users_list: list[dict]) -> None:
    restore_names(users_list)

    assert users_list[0]["first_name"] == "Mark"


def test_first_name_does_not_exist(users_list: list[dict]) -> None:
    restore_names(users_list)

    assert users_list[1]["first_name"] == "Mark"
