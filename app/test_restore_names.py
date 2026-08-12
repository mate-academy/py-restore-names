from app.restore_names import restore_names


def test_restore_names_when_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_restore_names_when_first_name_missing_key() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_restore_names_preserves_existing_first_name() -> None:
    users = [
        {
            "first_name": "Sarah",
            "last_name": "Connor",
            "full_name": "Sarah Connor",
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Sarah",
            "last_name": "Connor",
            "full_name": "Sarah Connor",
        }
    ]


def test_restore_names_multiple_users() -> None:
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
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
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
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
    ]


def test_restore_names_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_names_returns_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    result = restore_names(users)
    assert result is None
