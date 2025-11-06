from app.restore_names import restore_names


def test_restore_names_basic() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users == [
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


def test_restore_names_existing_names_not_changed() -> None:
    users = [
        {"first_name": "Anna", "last_name": "Stone", "full_name": "Anna Stone"},
    ]
    original = users.copy()
    restore_names(users)
    assert users == original


def test_restore_names_empty_first_name() -> None:
    users = [
        {
            "first_name": "",
            "last_name": "Taylor",
            "full_name": "Chris Taylor",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Chris"


def test_restore_names_extra_spaces_in_full_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Brown",
            "full_name": "  Lucy   Brown  ",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Lucy"


def test_restore_names_missing_full_name() -> None:
    users = [{"first_name": None, "last_name": "Unknown"}]
    restore_names(users)
    assert users == [{"first_name": None, "last_name": "Unknown"}]


def test_restore_names_multiple_words_in_full_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Jr.",
            "full_name": "John Doe Jr.",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_restore_names_in_place_mutation() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Rogers",
            "full_name": "Steve Rogers",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Steve"
