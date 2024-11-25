
from app.restore_names import restore_names


def test_no_change_for_existing_first_name() -> None:
    users = [
        {"last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]

    restore_names(users)

    expected = [
        {"first_name": "Jack", "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]

    assert users == expected


def test_mixed_first_name_states() -> None:
    users = [
        {"first_name": None, "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]

    restore_names(users)

    expected = [
        {"first_name": "Jack", "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams",
         "full_name": "Mike Adams"}]

    assert users == expected
