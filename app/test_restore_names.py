import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "users, first_users",
        [
            {
                "first_name": None,
                "full_name": "Jack Holy",
            },
            {
                "first_name": "Joe",
                "full_name": "Mike Adams",
            },
        ]
    )
    def test_restore_first_name_in_users(
            self,
            users: str,
            first_users: str
    ) -> None:
        result = first_users
        restore_names(result)
        assert first_users["first_name"] == result
