from app.restore_names import restore_names


def test_when_user_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_when_user_has_not_got_key_first_name() -> None:
    users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    restore_names(users)
    assert users[1]["first_name"] == "Mike"


def test_when_user_list_is_empty() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_when_user_in_users_is_empty_dict() -> None:
    users = [{}, {}]
    assert users[0] == {}
