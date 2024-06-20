import pytest
from app.restore_names import restore_names


def test_restore_names_with_missing_first_name() -> None:
    users = [
        {"last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]


def test_restore_names_with_none_first_name() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": None, "last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jack", "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name":
            "Adams", "full_name": "Mike Adams"},
    ]


def test_restore_names_with_existing_first_name() -> None:
    users = [
        {"first_name": "Jack", "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name":
            "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jack", "last_name":
            "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name":
            "Adams", "full_name": "Mike Adams"},
    ]


def test_restore_names_with_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_names_with_mixed_entries() -> None:
    users = [
        {"first_name": "Existing", "last_name": "User",
         "full_name": "Existing User"},
        {"first_name": None, "last_name": "Null",
         "full_name": "Restored Null"},
        {"last_name": "Missing", "full_name": "First Missing"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Existing", "last_name": "User",
         "full_name": "Existing User"},
        {"first_name": "Restored", "last_name": "Null",
         "full_name": "Restored Null"},
        {"first_name": "First", "last_name": "Missing",
         "full_name": "First Missing"},
    ]


if __name__ == "__main__":
    pytest.main()
