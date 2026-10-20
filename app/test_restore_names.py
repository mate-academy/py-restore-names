import pytest
from app.restore_names import restore_names


def test_restore_name_when_none() -> None:
    users = [
        {"first_name": None, "full_name": "Peter Parker"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Peter"


def test_restore_name_when_missing() -> None:
    users = [
        {"full_name": "Bruce Wayne"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Bruce"


def test_restore_name_when_exists() -> None:
    users = [
        {"first_name": "Tom", "full_name": "Peter Parker"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Tom"


def test_restore_name_when_empty() -> None:
    users = [
        {"first_name": None, "full_name": ""},
    ]
    with pytest.raises(IndexError):
        restore_names(users)


def test_restore_multiple_names() -> None:
    users = [
        {"first_name": None, "full_name": "Peter Parker"},
        {"full_name": "Bruce Wayne"},
        {"first_name": "Anna", "full_name": "Anna smith"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Peter"
    assert users[1]["first_name"] == "Bruce"
    assert users[2]["first_name"] == "Anna"
