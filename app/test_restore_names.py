from app.restore_names import restore_names


def test_restore_names_empty_users() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_names_missing_names() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe"
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe"

        }
    ]


def test_restore_names_no_change() -> None:
    users = [
        {
            "first_name": "Alice",
            "last_name": "Wonderland",
            "full_name": "Alice Wonderland"
        },
        {
            "first_name": "Bob",
            "last_name": "Builder",
            "full_name": "Bob Builder"
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Alice",
            "last_name": "Wonderland",
            "full_name": "Alice Wonderland"
        },
        {
            "first_name": "Bob",
            "last_name": "Builder",
            "full_name": "Bob Builder"
        }
    ]


def test_restore_names_duplicate_full_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Doe",
            "full_name": "John Doe"
        },
        {
            "first_name": None,
            "last_name": "Doe",
            "full_name": "John Doe"
        },
        {
            "first_name": None,
            "last_name": "Doe",
            "full_name": "Jane Doe"
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe"
        },
        {
            "first_name": None,
            "last_name": "Doe",
            "full_name": "John Doe"
        },
        {
            "first_name": "Jane",
            "last_name": "Doe",
            "full_name": "Jane Doe"
        }
    ]
