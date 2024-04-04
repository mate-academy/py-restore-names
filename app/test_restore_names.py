from app.restore_names import restore_names


def test_name_is_none() -> None:
    users = [{
        "first_name": None,
        "full_name": "Jack Holy",
    }]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_name_is_missing() -> None:
    users = [{
        "full_name": "Mike Adams",
    }]
    restore_names(users)
    assert users[0]["first_name"]
