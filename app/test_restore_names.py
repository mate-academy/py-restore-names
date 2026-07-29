from app.restore_names import restore_names


def test_restore_names_when_first_name_is_none() -> None:
    users = [{
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }]
    restore_names(users)
    assert users == [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"}
    ]


def test_restore_names_when_first_name_is_missing() -> None:
    users = [{"last_name": "Adams", "full_name": "Mike Adams"}]
    restore_names(users)
    assert users == [
        {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"}
    ]


def test_restore_names_does_not_overwrite_existing_first_name() -> None:
    users = [{
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }]
    restore_names(users)
    assert users == [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"}
    ]


def test_restore_names_with_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_names_with_multiple_mixed_users() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe"
        },
    ]
