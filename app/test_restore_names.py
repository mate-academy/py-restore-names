from app.restore_names import restore_names


def test_restores_without_first_name() -> None:
    users = [
        {
            "last_name": "Smith",
            "full_name": "John Smith",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_restores_with_none_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "John Smith",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_keeps_existing_first_name() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "John Smith",
        },
        {
            "first_name": "John",
            "last_name": "Black",
            "full_name": "Adam Black"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "John"
