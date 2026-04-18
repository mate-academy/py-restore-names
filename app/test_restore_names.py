from app.restore_names import restore_names


def test_restore_names_none_value() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Alyssa Holy",
        }
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Alyssa",
            "last_name": "Holy",
            "full_name": "Alyssa Holy",
        }
    ]


def test_restore_names_when_key_is_missing() -> None:
    users = [
        {
            "last_name": "Holy",
            "full_name": "Alyssa Holy",
        }
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Alyssa",
            "last_name": "Holy",
            "full_name": "Alyssa Holy",
        }
    ]
