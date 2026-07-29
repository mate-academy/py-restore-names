from app.restore_names import restore_names


def test_restore_names_with_none_first_name() -> None:
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


def test_restore_names_without_first_name() -> None:
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


def test_restore_names_with_valid_first_name() -> None:
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


def test_restore_names_multiple_users() -> None:
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
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
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
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
    ]
