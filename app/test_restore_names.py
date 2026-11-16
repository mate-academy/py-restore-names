from app.restore_names import restore_names


def test_restore_names_when_first_name_is_missing() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike John Adams",
        }
    ]

    result = restore_names(users)

    assert result is None
    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike John Adams",
        }
    ]


def test_restore_names_when_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    result = restore_names(users)

    assert result is None
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_restore_names_preserves_existing_first_name() -> None:
    users = [
        {
            "first_name": "Jane",
            "last_name": "Doe",
            "full_name": "Jane Doe",
        }
    ]

    result = restore_names(users)

    assert result is None
    assert users == [
        {
            "first_name": "Jane",
            "last_name": "Doe",
            "full_name": "Jane Doe",
        }
    ]


def test_restore_names_with_empty_users() -> None:
    users = []

    assert restore_names(users) is None
    assert users == []
