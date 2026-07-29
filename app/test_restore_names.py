from typing import Dict, List, Optional

from restore_names import restore_names


def test_restore_names_sets_missing_and_none_first_name() -> None:
    users: List[Dict[str, Optional[str]]] = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]

    ret = restore_names(users)

    assert ret is None
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
    ]


def test_restore_names_keeps_existing_first_name() -> None:
    users: List[Dict[str, str]] = [
        {"first_name": "Anna", "last_name": "Holy", "full_name": "Anna Holy"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Anna"


def test_restore_names_trims_and_uses_first_token() -> None:
    users: List[Dict[str, Optional[str]]] = [
        {
            "first_name": None,
            "last_name": "Adams",
            "full_name": "  Mike   Adams  ",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_names_when_key_absent() -> None:
    users: List[Dict[str, str]] = [
        {"last_name": "Doe", "full_name": "John Doe"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"
