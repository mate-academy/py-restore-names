from app.restore_names import restore_names


def test_restore_when_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_when_first_name_is_missing() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_do_not_overwrite_existing_first_name() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "Mike Adams"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_empty_users_list() -> None:
    users = []
    result = restore_names(users)
    assert users == []
    assert result is None


def test_function_returns_none() -> None:
    users = [{"full_name": "Jack Holy"}]
    result = restore_names(users)
    assert result is None


def test_other_fields_are_preserved() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users[0]["last_name"] == "Holy"
    assert users[0]["full_name"] == "Jack Holy"


def test_multiple_users_mixed_cases() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
    ]
    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "John"


def test_full_name_with_multiple_words() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "Anna Maria Smith",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Anna"
