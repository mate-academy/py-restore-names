import pytest
from typing import List

from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.fixture()
    def users_template_expected(self) -> List[dict]:
        return [
            {
                "first_name": "Anna",
                "last_name": "Holy",
                "full_name": "Anna Maria Holy",
            }
        ]

    @pytest.mark.parametrize(
        "users",
        [
            pytest.param(
                [
                    {
                        "first_name": None,
                        "last_name": "Holy",
                        "full_name": "Anna Maria Holy",
                    }
                ],
                id="should reset `first_name` when first_name is None"
            ),
            pytest.param(
                [
                    {
                        "last_name": "Holy",
                        "full_name": "Anna Maria Holy",
                    }
                ],
                id="should reset `first_name` when first_name is missing"
            ),
            pytest.param(
                [
                    {
                        "first_name": None,
                        "last_name": "Holy",
                        "full_name": "Anna Maria Holy",
                    }
                ],
                id="should take first word from `full_name`"
            ),
        ]
    )
    def test_restore_names(
            self,
            users_template_expected: List[dict],
            users: List[dict]
    ) -> None:
        restore_names(users)
        assert users_template_expected == users
