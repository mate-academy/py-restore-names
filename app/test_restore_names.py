from app.restore_names import restore_names


def test_1() -> None:
    user = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(user)
    assert user[0]["first_name"] == "Jack"


def test_2() -> None:
    user = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(user)
    assert user[0]["first_name"] == "Jack"
