from app.restore_names import restore_names


def test_should_restore_first_name_when_it_is_none() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_should_restore_first_name_when_key_is_missing() -> None:
    users = [{"last_name": "Adams", "full_name": "Mike Adams"}]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_should_not_change_existing_first_name() -> None:
    users = [
        {
            "first_name": "Johnny",
            "last_name": "Smith",
            "full_name": "John Smith",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Johnny"


def test_should_restore_names_for_all_users_as_in_example() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
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
    ]


def test_should_not_return_anything() -> None:
    users = [{"last_name": "Adams", "full_name": "Mike Adams"}]
    assert restore_names(users) is None
