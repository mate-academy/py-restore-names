import pytest
from typing import List
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "users, expected",
        [
            pytest.param(
                [
                    {
                        "first_name": None,
                        "last_name": "Holy",
                        "full_name": "Jack Holy",
                    }
                ],
                [
                    {
                        "first_name": "Jack",
                        "last_name": "Holy",
                        "full_name": "Jack Holy",
                    }
                ],
                id="Add Jack to first_name"
            ),
            pytest.param(
                [
                    {
                        "last_name": "Adams",
                        "full_name": "Mike Adams",
                    }
                ],
                [
                    {
                        "first_name": "Mike",
                        "last_name": "Adams",
                        "full_name": "Mike Adams",
                    }
                ],
                id="Add Mike to first_name"
            ),
        ]
    )
    def test_restore_names(self,
                           users: List[dict],
                           expected: list) -> None:
        restore_names(users)
        assert users == expected
