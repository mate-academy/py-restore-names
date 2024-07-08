import pytest
from app.restore_names import restore_names
from typing import List, Dict


class TestRestoreNames:
    @pytest.mark.parametrize(
        "actual_users, expected_users",
        [
            pytest.param([
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ], [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ], id="should rename None to Jack"),
            pytest.param([
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ], [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ], id="should create first name if it doesn't exist")
        ],
    )
    def test_restore_names(self,
                           actual_users: List[Dict],
                           expected_users: List[Dict]) -> None:
        restore_names(actual_users)
        assert actual_users == expected_users

    @pytest.mark.parametrize(
        "users",
        [
            pytest.param(1, id="should raise erroe if integer")
        ]
    )
    def test_should_raise_error_if_not_list_of_dict(
            self,
            users: List[Dict]) -> None:
        with pytest.raises(TypeError):
            restore_names(users)
