import pytest
from app.restore_names import restore_names

class TestModify:
    @pytest.mark.parametrize(
        "users, result_users",
        [
            pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            id="Test1"
        ),
        ])
    def test_modify(self, users, result_users):
        restore_names(users)
        assert users == result_users

