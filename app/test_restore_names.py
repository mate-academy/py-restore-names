import pytest
from app.restore_names import restore_names


@pytest.fixture
def users_template() -> list:
    users = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    return users


@pytest.fixture
def users_restored() -> list:
    users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    return users


def test_restore_names_when_all_first_names_equals_none(
        users_template: list,
        users_restored: list
) -> None:
    users_template[0]["first_name"] = None
    users_template[1]["first_name"] = None
    restore_names(users_template)
    assert users_template == users_restored


def test_restore_names_when_is_no_first_names(
        users_template: list,
        users_restored: list
) -> None:
    restore_names(users_template)
    assert users_template == users_restored


def test_restore_names_when_is_no_first_name_or_when_equals_none(
        users_template: list,
        users_restored: list
) -> None:
    users_template[0]["first_name"] = None
    restore_names(users_template)
    assert users_template == users_restored
