from app.restore_names import restore_names


def test_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_surname": "Smith",
            "full_name": "John Smith"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_first_name_is_missing() -> None:
    users = [
        {
            "last_surname": "Smith",
            "full_name": "John Smith"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"
