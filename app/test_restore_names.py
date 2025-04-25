import pytest
from app.restore_names import restore_names

class TestRestoreNames:
    @pytest.mark.parametrize(
        "users",
        [
            {
                "first_name": None,
                "full_name": "Jack Holy",
            },
            {
                "first_name": "Mike",
                "full_name": "Mike Adams",
            },

        {
            "first_name": "Jack",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "full_name": "Mike Adams",
        },
    ]
    )
    def test_restore_first_name_in_users(self, users, expected_first_name):
        result = expected_first_name
        restore_names(users)
        assert expected_first_name["first_name"] == result
