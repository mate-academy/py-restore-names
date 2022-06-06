import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "users,expected",
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
                id="should have 'first_name' != None"),
            pytest.param(
                [
                    {
                        "last_name": "Adams",
                        "full_name": "Mike Adams",
                    },
                ],
                [
                    {
                        "first_name": "Mike",
                        "last_name": "Adams",
                        "full_name": "Mike Adams",
                    },
                ],
                id="should have key 'first_name'")
        ]
    )
    def test_restore_names(self, users, expected):
        user_data = users
        restore_names(user_data)
        assert user_data == expected
