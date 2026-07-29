from app.restore_names import restore_names


def test_restore_names_basic() -> None:
    users = [
        {"first_name": None,
         "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"last_name": "Adams",
         "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jack",
         "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"first_name": "Mike",
         "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]


def test_restore_names_no_missing() -> None:
    users = [
        {"first_name": "John",
         "last_name": "Smith",
         "full_name": "John Smith"},
        {"first_name": "Anna",
         "last_name": "Lee",
         "full_name": "Anna Lee"},
    ]
    original = [user.copy() for user in users]
    restore_names(users)
    assert users == original  # не повинно нічого змінитися


def test_restore_names_partial_missing() -> None:
    users = [
        {"first_name": "Emma",
         "last_name": "Stone",
         "full_name": "Emma Stone"},
        {"first_name": None,
         "last_name": "Brown",
         "full_name": "Lily Brown"},
    ]
    restore_names(users)
    assert users[1]["first_name"] == "Lily"


def test_restore_names_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_names_missing_first_name_key() -> None:
    users = [
        {"last_name": "Musk",
         "full_name": "Elon Musk"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Elon"
