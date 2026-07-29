import pytest
from typing import List
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_dict, expected_result",
    [
        pytest.param(
            [
                {
                    "first_name": "Luke",
                    "last_name": "Skywalker",
                    "full_name": "Luke Skywalker",
                }
            ],
            [
                {
                    "first_name": "Luke",
                    "last_name": "Skywalker",
                    "full_name": "Luke Skywalker",
                }
            ],
            id="should not add first name if it already exists",
        ),
        pytest.param(
            [
                {
                    "last_name": "Organa",
                    "full_name": "Leia Organa"
                }
            ],
            [
                {
                    "first_name": "Leia",
                    "last_name": "Organa",
                    "full_name": "Leia Organa"
                }
            ],
            id="should add first name if it doesn't exist"),
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Solo",
                    "full_name": "Han Solo"
                }
            ],
            [
                {
                    "first_name": "Han",
                    "last_name": "Solo",
                    "full_name": "Han Solo"
                }
            ],
            id="should add first name if it is None"),
        pytest.param(
            [
                {
                    "last_name": "Skywalker",
                    "first_name": None,
                    "full_name": "Luke Skywalker"
                }
            ],
            [
                {
                    "last_name": "Skywalker",
                    "first_name": "Luke",
                    "full_name": "Luke Skywalker"
                }
            ],
            id="should add first name if it is placed second"
        ),
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Skywalker",
                    "full_name": "Luke Skywalker"
                },
                {
                    "last_name": "Organa",
                    "full_name": "Leia Organa"
                }
            ],
            [
                {
                    "first_name": "Luke",
                    "last_name": "Skywalker",
                    "full_name": "Luke Skywalker"
                },
                {
                    "first_name": "Leia",
                    "last_name": "Organa",
                    "full_name": "Leia Organa"
                }
            ],
            id="should add first name in few dicts"
        ),
    ]
)
def test_restore_names(
        users_dict: List[dict],
        expected_result: List[dict]
) -> None:
    restore_names(users_dict)
    assert users_dict == expected_result
