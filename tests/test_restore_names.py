from app.restore_names import restore_names


def test_restore_names_sets_missing_first_name() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Jane",
            "last_name": "Doe",
            "full_name": "Jane Doe",
        },
    ]

    result = restore_names(users)

    assert result is None
    assert users[0]["first_name"] == "Mike"
    assert users[0]["last_name"] == "Adams"
    assert users[0]["full_name"] == "Mike Adams"
    assert users[1]["first_name"] == "Jane"


def test_restore_names_sets_none_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[0]["last_name"] == "Holy"
    assert users[0]["full_name"] == "Jack Holy"


def test_restore_names_preserves_empty_first_name() -> None:
    users = [
        {
            "first_name": "",
            "last_name": "Smith",
            "full_name": "Empty Smith",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == ""
    assert users[0]["last_name"] == "Smith"
    assert users[0]["full_name"] == "Empty Smith"


def test_restore_names_uses_first_token_of_full_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Watson",
            "full_name": "Mary Jane Watson",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Mary"
