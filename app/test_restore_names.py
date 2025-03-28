from app.restore_names import restore_names


def test_restore_missing_first_names() -> None:
    users = [
        {"first_name": None,
         "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams",
         "full_name": "Mike Adams"},
    ]

    restore_names(users)

    assert users == [
        {"first_name": "Jack",
         "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike",
         "last_name": "Adams", "full_name": "Mike Adams"},
    ]


def test_no_changes_if_first_name_exists() -> None:
    users = [
        {"first_name": "Emma",
         "last_name": "Stone", "full_name": "Emma Stone"},
        {"first_name": "Chris",
         "last_name": "Evans", "full_name": "Chris Evans"},
    ]

    restore_names(users)

    assert users == [
        {"first_name": "Emma",
         "last_name": "Stone", "full_name": "Emma Stone"},
        {"first_name": "Chris",
         "last_name": "Evans", "full_name": "Chris Evans"},
    ]


def test_restore_names_mixed_cases() -> None:
    users = [
        {"first_name": None,
         "last_name": "Wayne", "full_name": "Bruce Wayne"},
        {"first_name": "Clark",
         "last_name": "Kent", "full_name": "Clark Kent"},
        {"first_name": None,
         "last_name": "Parker", "full_name": "Peter Parker"},
    ]

    restore_names(users)

    assert users == [
        {"first_name": "Bruce",
         "last_name": "Wayne", "full_name": "Bruce Wayne"},
        {"first_name": "Clark",
         "last_name": "Kent", "full_name": "Clark Kent"},
        {"first_name": "Peter",
         "last_name": "Parker", "full_name": "Peter Parker"},
    ]
