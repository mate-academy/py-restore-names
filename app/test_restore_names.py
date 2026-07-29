from typing import Any

import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> dict:
    return {
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }


def test_restore_names_when_name_is_none(users_template: Any) -> None:
    users_template["first_name"] = None
    restore_names([users_template])
    assert users_template["first_name"] == "Jack"


def test_restore_names_when_name_is_non_exist(users_template: Any) -> None:
    del users_template["first_name"]
    restore_names([users_template])
    assert users_template["first_name"] == "Jack"
