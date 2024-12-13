import pytest
from typing import List
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "users, expected_result",
        [
            pytest.param([{
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }],
                [{
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }],
                id="should update 'first_name' if it hasn't value"),
            pytest.param([{
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }],
                [{
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }],
                id="should create 'first_name' if it isn't exist"),
            pytest.param([{
                "first_name": "William",
                "last_name": "Gates",
                "full_name": "Bill Gates",
            }],
                [{
                    "first_name": "William",
                    "last_name": "Gates",
                    "full_name": "Bill Gates",
                }],
                id="shouldn't change anything if value already exist"),
        ]
    )
    def test_restore_names(
            self,
            users: List[dict],
            expected_result: List[dict],
    ) -> None:
        restore_names(users)
        assert users == expected_result
