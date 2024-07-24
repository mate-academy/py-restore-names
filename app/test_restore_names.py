import pytest
from app.restore_names import restore_names

class TestRestoreNames:
    @pytest.mark.parametrize(
        "users,restored_users",
        [
            (
                [
                    {"first_name": None,
                     "last_name": "Smith",
                     "full_name": "James Smith"}
                ],
                [
                    {"first_name": "James",
                     "last_name": "Smith",
                     "full_name": "James Smith"}
                ]
            ),
            (
                [
                    {"last_name": "Rodgers",
                     "full_name": "Steve Rodgers"}
                ],
                [
                    {"first_name": "Steve",
                     "last_name": "Rodgers",
                     "full_name": "Steve Rodgers"}
                ]
            )
        ]
    )
    def test_restore_correct_first_name(self, users: list[dict], restored_users: list[dict]) -> None:
        assert restore_names(users) is None
        assert users == restored_users
