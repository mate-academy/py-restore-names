from app.restore_names import restore_names


def test_first_name_equal_to_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Black",
            "full_name": "Bob Black"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Bob"


def test_first_name_is_missing() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]
    restore_names(users)
    assert "first_name" in users[0]
    assert users[0]["first_name"] == "Mike"
