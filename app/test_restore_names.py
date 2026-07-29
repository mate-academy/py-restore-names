import pytest

from app.restore_names import restore_names


def test_if_func_restores_name_from_full_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    result = restore_names(users)

    assert result is None
    assert users[0]["first_name"] == "Jack"


def test_when_first_name_is_missing() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    result = restore_names(users)

    assert result is None
    assert users[0]["first_name"] == "Mike"


def test_does_not_change_existing_first_name() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    result = restore_names(users)

    assert result is None
    assert users[0]["first_name"] == "John"


def test_when_parameter_users_is_empty() -> None:
    with pytest.raises(KeyError):
        restore_names([])
