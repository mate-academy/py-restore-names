from app.restore_names import restore_names


def test_restore_names_when_first_name_is_missing() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_names_when_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_should_not_change_existing_first_name() -> None:
    # If first_name is already present and not None, keep it
    users = [
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "Johnny Smith",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_restore_names_for_multiple_users_in_list() -> None:
    users = [
        {
            "first_name": None,
            "full_name": "Alice Smith",
        },
        {
            "full_name": "Bob Jones",
        },
        {
            "first_name": "Charlie",
            "full_name": "Charles Brown",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Alice"
    assert users[1]["first_name"] == "Bob"
    assert users[2]["first_name"] == "Charlie"
