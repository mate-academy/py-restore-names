from app.restore_names import restore_names


def test_if_first_name_is_missing() -> None:
    users = [{
        "last_name": "Adams",
        "full_name": "Mike Adams",
    }]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_if_first_name_is_none() -> None:
    users = [{
        "first_name": None,
        "last_name": "Bobcat",
        "full_name": "Anton Bobcat",
    }]
    restore_names(users)
    assert users[0]["first_name"] == "Anton"
