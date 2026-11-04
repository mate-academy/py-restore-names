from app.restore_names import restore_names

from typing import Dict, List


def test_restore_names_when_none_and_missing() -> None:
    users: List[Dict[str, str | None]] = [
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


def test_restore_names_keeps_existing() -> None:
    # Caso 2: Si ya tiene un first_name válido, no debe tocarlo
    users: List[Dict[str, str]] = [
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
