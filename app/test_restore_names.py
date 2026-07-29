from app.restore_names import restore_names


def test__names_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holly",
            "full_name": "Jack Holly",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test__names_is_missing() -> None:
    users = [
        {
            "last_name": "Holly",
            "full_name": "Jack Holly",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test__names_is_right() -> None:
    users = [
        {
            "first_name": "Jack",
            "last_name": "Holly",
            "full_name": "Jack Holly",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
