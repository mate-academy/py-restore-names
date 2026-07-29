from __future__ import annotations

import pytest

from app.restore_names import restore_names


@pytest.fixture()
def user_before() -> None:
    users_before = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }, ]
    yield users_before
    print(user_before)


@pytest.fixture()
def user_after() -> None:
    users_after = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }, ]
    yield users_after
    print(users_after)


def test_restore_names(user_before: list[dict],
                       user_after: list[dict]) -> None:
    restore_names(user_before)
    assert user_before == user_after
