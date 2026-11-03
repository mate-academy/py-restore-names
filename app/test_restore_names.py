def test_restore_names_none_and_missing() -> None:
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
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_restore_names_already_present() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_restore_names_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_names_compound_full_name() -> None:
    users = [
        {
            "first_name": None,
            "full_name": "Anna Maria Souza",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Anna"


def test_restore_names_returns_none() -> None:
    users = [{"first_name": None, "full_name": "Test User"}]
    result = restore_names(users)
    assert result is None
