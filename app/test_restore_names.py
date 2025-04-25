import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "users, expected_first_name",
        [
            (
                [{"first_name": None, "full_name": "Jack Holy"}],
                "Jack"
            ),
            (
                [{"last_name": "Adams", "full_name": "Mike Adams"}],
                "Mike"
            ),
            (
                [{"first_name": "Jack", "full_name": "Jack Holy"}],
                "Jack"
            ),
            (
                [{"first_name": "Mike", "full_name": "Mike Adams"}],
                "Mike"
            ),
        ]
    )
    def test_restore_first_name_in_users(
            self,
            users: list[dict],
            expected_first_name: str
    ) -> None:
        restore_names(users)
        assert users[0]["first_name"] == expected_first_name
