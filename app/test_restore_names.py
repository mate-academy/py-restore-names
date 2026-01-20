from app.restore_names import restore_names


def test_user_first_name_is_none() -> None:
    users = [{
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }]
    restore_names(users)
    assert users == [{
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"}]


def test_there_is_no_user_first_name() -> None:
    users = [{
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }]
    restore_names(users)
    assert users == [{
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"}]
