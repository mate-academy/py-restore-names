from app.restore_names import restore_names


def test_restore_only_missing_names() -> None:
    users = [
        {
            "last_name": "Holy",
            "full_name": "Martin Holy",
        }
    ]
    expected = [
        {
            "first_name": "Martin",
            "last_name": "Holy",
            "full_name": "Martin Holy",
        }
    ]
    restore_names(users)
    assert users == expected


def test_restore_only_none_names() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Martin Holy",
        }
    ]
    expected = [
        {
            "first_name": "Martin",
            "last_name": "Holy",
            "full_name": "Martin Holy",
        }
    ]
    restore_names(users)
    assert users == expected
