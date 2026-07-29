import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "users, expected",
        [
            ([{
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy"
            }], "Jack"),
            ([{
                "last_name": "Adams", "full_name": "Mike Adams"
            }], "Mike"),
        ],
        ids=[
            "First name is None",
            "First name is empty",
        ]
    )
    def test_restore_empty_names(self, users: list, expected: str) -> None:
        restore_names(users)

        assert users[0]["first_name"] == expected
