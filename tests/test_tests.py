from typing import List

import pytest

from app import restore_names


def test_restore_only_missing_names() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names.restore_names(users)

    assert users[0]["first_name"] == "Jack"


def test_restore_only_none_names() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    restore_names.restore_names(users)

    assert users[0]["first_name"] == "Mike"
