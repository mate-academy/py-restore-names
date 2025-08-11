from app.restore_names import restore_names


def test_restore_names_none_or_missing_first_name() -> None:
    users = [
        {"first_name": None, "last_name": "Doe", "full_name": "John Doe"},
        {"last_name": "Ermentraut", "full_name": "Mike Ermentraut"},
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe"
        },
        {
            "first_name": "Mike",
            "last_name": "Ermentraut",
            "full_name": "Mike Ermentraut"
        },
    ]
