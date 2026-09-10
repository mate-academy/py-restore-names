from copy import deepcopy

import pytest
from app.restore_names import restore_names


@pytest.fixture()
def data_template() -> list[dict]:
    users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    return users


def test_no_restore_if_first_name_exist(data_template: list[dict]) -> None:
    expected = deepcopy(data_template)
    restore_names(data_template)
    assert data_template == expected


def test_restore_if_first_name_is_none(data_template: list[dict]) -> None:
    expected = deepcopy(data_template)
    data_template[0]["first_name"] = None
    restore_names(data_template)
    assert data_template == expected


def test_restore_if_first_name_not_exist(data_template: list[dict]) -> None:
    expected = deepcopy(data_template)
    del data_template[0]["first_name"]
    restore_names(data_template)
    assert data_template == expected


def test_restore_names_multiple_users() -> None:
    users = [
        {"first_name": "Jack", "full_name": "Jack Holy"},
        {"first_name": None, "full_name": "John Doe"},
        {"full_name": "Anna Smith"},
    ]
    restore_names(users)
    assert [user["first_name"] for user in users] == ["Jack", "John", "Anna"]
