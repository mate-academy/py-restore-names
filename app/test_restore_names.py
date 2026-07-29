import pytest
from app.restore_names import restore_names


class TestRestoreNames:

    @pytest.mark.parametrize(
        "user, expected_user",
        [
            (
                [{"first_name": None, "full_name": "Jack Holy"}],
                [{"first_name": "Jack", "full_name": "Jack Holy"}]
            ),
            (
                [{"full_name": "Nick Holy"}],
                [{"first_name": "Nick", "full_name": "Nick Holy"}]
            ),
            (
                [{"first_name": "Mike", "full_name": "Jack Holy"}],
                [{"first_name": "Mike", "full_name": "Jack Holy"}]
            )
        ],
        ids=[
            "First name should change for Jack",
            "Should create a key first_name with name Nick",
            "Should not change first name"
        ]
    )
    def test_expected_result(
            self, user: list[dict], expected_user: list[dict]
    ) -> None:
        restore_names(user)
        assert user == expected_user
