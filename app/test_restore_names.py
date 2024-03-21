import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "user, expected_user",
        [
            (
                [{"first_name": None, "full_name": "Jack Holy"}],
                [{"first_name": "Jack", "full_name": "Jack Holy"}],
            ),
            (
                [{"full_name": "Mike Adams"}],
                [{"first_name": "Mike", "full_name": "Mike Adams"}],
            ),
            (
                [{"first_name": "Mike", "full_name": "Mike Adams"}],
                [{"first_name": "Mike", "full_name": "Mike Adams"}]
            )

        ],
        ids=[
            "First name should be changed",
            "Should create a key first_name with name Mike",
            "First name shouldn`t be changed"
        ]
    )
    def test_restore_user(self, user: list[dict], expected_user: list[dict]) -> None:
        restore_names(user)
        assert user == expected_user
