import pytest
from app.restore_names import restore_names


def test_restore_names() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack", "Failed on user 1"
    assert users[1]["first_name"] == "Mike", "Failed on user 2"


def test_restore_names_no_full_name() -> None:
    users = [
        {"first_name": None},
        {"first_name": ""}
    ]
    with pytest.raises(KeyError):
        restore_names(users)


def test_restore_name_empty_list() -> None:
    users = []
    restore_names(users)
