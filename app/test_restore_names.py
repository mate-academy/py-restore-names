from app.restore_names import restore_names


def test_restore_name_when_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_name_when_first_name_is_missing() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_do_not_change_existing_first_name() -> None:
    users = [
        {
            "first_name": "Bob",
            "last_name": "Smith",
            "full_name": "Bob Smith",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Bob"


def test_empty_users_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_mixed_users() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Ann",
            "last_name": "Brown",
            "full_name": "Ann Brown",
        },
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Ann",
            "last_name": "Brown",
            "full_name": "Ann Brown",
        },
    ]
