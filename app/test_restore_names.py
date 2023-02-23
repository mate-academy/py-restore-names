import pytest
from app.restore_names import restore_names


correct_users = [
    {
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"
    },
    {
        "first_name": "Mike",
        "last_name": "Adams",
        "full_name": "Mike Adams"
    }
]


def test_return_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": None,
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]
    assert restore_names(users) is None


def test_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": None,
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]
    restore_names(users)
    assert users == correct_users


def test_first_name_is_missing() -> None:
    users = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]
    restore_names(users)
    assert users == correct_users


def test_users_full_name_without_space() -> None:
    users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "MikeAdams"
        }
    ]
    with pytest.raises(ValueError):
        restore_names(users)


def test_users_missing_full_name() -> None:
    users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
        }
    ]
    with pytest.raises(KeyError):
        restore_names(users)
