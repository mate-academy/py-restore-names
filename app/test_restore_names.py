from app.restore_names import restore_names


def test_restore_names_none_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    expected_users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(users)
    assert users == expected_users, "The first_name should be restored " \
                                    "from full_name when it is None"


def test_restore_names_missing_first_name() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    expected_users = [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    restore_names(users)
    assert users == expected_users, "The first_name should be " \
                                    "restored from full_name " \
                                    "when it is missing"


def test_restore_names_all_correct() -> None:
    users = [
        {
            "first_name": "Jane",
            "last_name": "Doe",
            "full_name": "Jane Doe",
        }
    ]

    expected_users = [
        {
            "first_name": "Jane",
            "last_name": "Doe",
            "full_name": "Jane Doe",
        }
    ]

    restore_names(users)
    assert users == expected_users, "The first_name should remain unchanged " \
                                    "if it already exists and is not None"


def test_restore_names_mixed_cases() -> None:
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
            "first_name": "Sarah",
            "last_name": "Smith",
            "full_name": "Sarah Smith",
        }
    ]

    expected_users = [
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
            "first_name": "Sarah",
            "last_name": "Smith",
            "full_name": "Sarah Smith",
        }
    ]

    restore_names(users)
    assert users == expected_users, "The function should restore " \
                                    "missing or None first names " \
                                    "and leave correct ones unchanged"
