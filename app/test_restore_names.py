import pytest
from app.restore_names import restore_names


@pytest.fixture
def users_template() -> list:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Emily",
            "last_name": "Stone",
            "full_name": "Emily Stone",
        },
    ]


def test_restore_none_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_missing_first_name_key() -> None:
    users = [{"last_name": "Adams", "full_name": "Mike Adams"}]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_do_not_change_valid_first_name() -> None:
    users = [
        {
            "first_name": "Emily",
            "last_name": "Stone",
            "full_name": "Emily Stone"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Emily"


def test_restore_only_missing_fields(users_template: list) -> None:
    restore_names(users_template)
    assert users_template[0]["first_name"] == "Jack"   # було None
    assert users_template[1]["first_name"] == "Mike"   # не було ключа
    assert users_template[2]["first_name"] == "Emily"  # вже правильне


def test_restore_with_edge_case_full_name_one_word() -> None:
    users = [{"last_name": "Unknown", "full_name": "Solo"}]
    restore_names(users)
    assert users[0]["first_name"] == "Solo"
