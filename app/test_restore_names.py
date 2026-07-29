import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "name, expected",
        [
            (
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                },
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ),
            (
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                },
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                }
            )
        ]
    )
    def test_restore_name_in_users(
            self,
            expected: dict,
            name: dict
    ) -> None:
        users = [name]
        restore_names(users)
        assert users[0] == expected
