from copy import deepcopy

import pytest

from app.restore_names import restore_names


@pytest.fixture()
def users_to_restore() -> list[dict]:
    return [
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
            "first_name": "Bob",
            "last_name": "Smith",
            "full_name": "Bob Smith",
        },
    ]


@pytest.fixture()
def restored_users(users_to_restore: list[dict]) -> list[dict]:
    users = []

    for user in deepcopy(users_to_restore):
        user["first_name"] = user["full_name"].split()[0]
        users.append(user)

    return users


class TestRestoreNames:
    def test_restore_users(
            self,
            users_to_restore: list[dict],
            restored_users: list[dict],
    ) -> None:
        restore_names(users_to_restore)
        assert users_to_restore == restored_users, (
            "should restore first_name for each user"
        )
