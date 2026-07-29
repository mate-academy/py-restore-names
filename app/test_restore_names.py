from app.restore_names import restore_names


def test_restore_missing_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    expected_users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    restore_names(users)
    assert users == expected_users, (
        f"Expected {expected_users} but got {users}"
    )


def test_no_change_if_first_name_exists() -> None:
    users = [
        {
            "first_name": "Sarah",
            "last_name": "Connor",
            "full_name": "Sarah Connor",
        },
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]

    expected_users = [
        {
            "first_name": "Sarah",
            "last_name": "Connor",
            "full_name": "Sarah Connor",
        },
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]

    restore_names(users)
    assert users == expected_users, (
        "Function should not alter users with existing first names."
    )


def test_empty_list() -> None:
    users = []
    expected_users = []

    restore_names(users)
    assert users == expected_users, (
        "Function should handle an empty list correctly."
    )


def test_partial_name() -> None:
    users = [
        {
            "first_name": None,
            "full_name": "Alice",
        }
    ]

    expected_users = [
        {
            "first_name": "Alice",
            "full_name": "Alice",
        }
    ]

    restore_names(users)
    assert users == expected_users, (
        "Function should handle users with only a first name in full_name."
    )


def test_multiple_users_some_with_missing_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "Alice Smith",
        },
        {
            "first_name": "Bob",
            "last_name": "Brown",
            "full_name": "Bob Brown",
        },
        {
            "last_name": "Johnson",
            "full_name": "Charlie Johnson",
        },
    ]

    expected_users = [
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "full_name": "Alice Smith",
        },
        {
            "first_name": "Bob",
            "last_name": "Brown",
            "full_name": "Bob Brown",
        },
        {
            "first_name": "Charlie",
            "last_name": "Johnson",
            "full_name": "Charlie Johnson",
        }
    ]

    restore_names(users)
    assert users == expected_users, (
        f"Expected {expected_users} but got {users}"
    )
