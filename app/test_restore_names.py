from app.restore_names import restore_names


def test_restore_none_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Doe",
            "full_name": "John Doe"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_restore_missing_first_name() -> None:
    users = [
        {
            "last_name": "Smith",
            "full_name": "Alice Smith"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Alice"


def test_do_not_override_existing_first_name() -> None:
    users = [
        {
            "first_name": "Jane",
            "last_name": "Doe",
            "full_name": "Jane Doe"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jane"


def test_multiple_users_mixed_cases() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Black",
            "full_name": "Tom Black"
        },
        {
            "last_name": "White",
            "full_name": "Sarah White"
        },
        {
            "first_name": "Emily",
            "last_name": "Green",
            "full_name": "Emily Green"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Tom"
    assert users[1]["first_name"] == "Sarah"
    assert users[2]["first_name"] == "Emily"


def test_name_with_middle_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Brown",
            "full_name": "David James Brown"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "David"
