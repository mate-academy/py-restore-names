from app.restore_names import restore_names


def test_restore_names_fill_none_value():
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_none_value():
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]
    restore_names(users)
    assert "first_name" in users[0]
    assert users[0]["first_name"] == "Mike"
