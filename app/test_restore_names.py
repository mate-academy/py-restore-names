from typing import List, Dict, Any

import app.restore_names as main


def test_restore_first_name_when_value_is_none() -> None:
    users: List[Dict[str, Any]] = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    result = main.restore_names(users)

    assert result is None
    assert users[0]["first_name"] == "Jack"


def test_restore_first_name_when_key_is_missing() -> None:
    users: List[Dict[str, Any]] = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    result = main.restore_names(users)

    assert result is None
    assert users[0]["first_name"] == "Mike"


def test_do_not_override_existing_first_name() -> None:
    users: List[Dict[str, Any]] = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "Jack Doe",
        }
    ]

    main.restore_names(users)

    assert users[0]["first_name"] == "John"


def test_restore_first_name_for_multiple_users() -> None:
    users: List[Dict[str, Any]] = [
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
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Anna Smith",
        },
    ]

    main.restore_names(users)

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
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Anna Smith",
        },
    ]
