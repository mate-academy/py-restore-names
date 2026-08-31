from typing import Any, Dict, List
import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_users",
    [
        (
                [
                    {
                        "first_name": None,
                        "last_name": "Taylor",
                        "full_name": "Hope Taylor",
                    },
                    {
                        "last_name": "Miller",
                        "full_name": "Faith Miller",
                    },
                ],
                [
                    {
                        "first_name": "Hope",
                        "last_name": "Taylor",
                        "full_name": "Hope Taylor",
                    },
                    {
                        "first_name": "Faith",
                        "last_name": "Miller",
                        "full_name": "Faith Miller",
                    },
                ],
        ),
        (
                [
                    {
                        "first_name": "Love",
                        "last_name": "Davis",
                        "full_name": "Love Davis",
                    },
                ],
                [
                    {
                        "first_name": "Love",
                        "last_name": "Davis",
                        "full_name": "Love Davis",
                    },
                ],
        ),
        (
                [
                    {
                        "first_name": None,
                        "last_name": "Wilson",
                        "full_name": "Hope Faith Wilson",
                    },
                ],
                [
                    {
                        "first_name": "Hope",
                        "last_name": "Wilson",
                        "full_name": "Hope Faith Wilson",
                    },
                ],
        ),
        (
                [],
                [],
        ),
    ],
    ids=[
        "restore_missing_and_none_first_names",
        "do_not_modify_existing_first_name",
        "restore_first_name_from_multi_word_full_name",
        "handle_empty_user_list",
    ],
)
def test_restore_names(
        users: List[Dict[str, Any]],
        expected_users: List[Dict[str, Any]],
) -> None:
    restore_names(users)
    assert users == expected_users
