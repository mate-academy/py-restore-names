from unittest.mock import MagicMock

import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize("users, expected", [
    (
        [
            {"full_name": "John Doe", "first_name": None},
            {"full_name": "Jane Smith"}
        ],
        [
            {"full_name": "John Doe", "first_name": "John"},
            {"full_name": "Jane Smith", "first_name": "Jane"}
        ],
    ),
    (
        [
            {"full_name": "John Doe", "first_name": "Johnny"},
            {"full_name": "Jane Smith", "first_name": "Janie"}
        ],
        [
            {"full_name": "John Doe", "first_name": "Johnny"},
            {"full_name": "Jane Smith", "first_name": "Janie"}
        ]
    ),
    (
        [],
        []
    )
])
def test_restore_names(users: list, expected: list) -> None:
    restore_names(users)
    assert users == expected


def test_restore_names_with_mock() -> None:
    user1 = MagicMock()
    user1.__getitem__.side_effect = lambda key: \
        {"full_name": "John Doe", "first_name": None}[key]
    user2 = MagicMock()
    user2.__getitem__.side_effect = lambda key: \
        {"full_name": "Jane Smith"}[key]

    users = [user1, user2]

    restore_names(users)

    user1.__getitem__.assert_any_call("full_name")
    user2.__getitem__.assert_any_call("full_name")

    user1.__setitem__.assert_called_with("first_name", "John")
    user2.__setitem__.assert_called_with("first_name", "Jane")
