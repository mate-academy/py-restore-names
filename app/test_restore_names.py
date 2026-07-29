import pytest

from typing import List

from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> List[dict]:
    return [
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "John Smith",
        },
        {
            "last_name": "Dou",
            "full_name": "Mike Dou",
        }
    ]


def test_restore_names(users_template: List[dict]) -> None:
    restore_names(users_template)
    assert users_template == [
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "John Smith",
        },
        {
            "first_name": "Mike",
            "last_name": "Dou",
            "full_name": "Mike Dou",
        }
    ]
