from app.restore_names import restore_names


def test_restore_names_all_missing() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams",
         "full_name": "Mike Adams"},  # Missing first_name
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jack",
         "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike",
         "last_name": "Adams", "full_name": "Mike Adams"},
    ]


def test_restore_names_some_missing() -> None:
    users = [
        {"first_name": None,
         "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Anna",
         "last_name": "Smith", "full_name": "Anna Smith"},
        {"last_name": "Brown",
         "full_name": "Tom Brown"},  # Missing first_name
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jack",
         "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Anna",
         "last_name": "Smith", "full_name": "Anna Smith"},
        {"first_name": "Tom",
         "last_name": "Brown", "full_name": "Tom Brown"},
    ]


def test_restore_names_no_missing() -> None:
    users = [
        {"first_name": "Jack",
         "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Anna",
         "last_name": "Smith", "full_name": "Anna Smith"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jack",
         "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Anna",
         "last_name": "Smith", "full_name": "Anna Smith"},
    ]


def test_restore_names_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []
