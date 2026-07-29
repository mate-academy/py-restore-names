from app.restore_names import restore_names


def test_restore_names_with_first_name_as_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_restore_names_with_missing_first_name() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_restore_names_with_existing_first_name() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]


def test_restore_names_with_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_names_with_multiple_users() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "Alice Smith",
        },
        {
            "last_name": "Johnson",
            "full_name": "Bob Johnson",
        },
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "full_name": "Alice Smith",
        },
        {
            "first_name": "Bob",
            "last_name": "Johnson",
            "full_name": "Bob Johnson",
        },
    ]
