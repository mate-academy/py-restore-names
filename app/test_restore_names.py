import copy
import pytest
from app import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "users,expected_data",
        [
            (
                [{"first_name": None, "full_name": "Jack Holy"}],
                [{"first_name": "Jack", "full_name": "Jack Holy"}]
            ),
            (
                [{"full_name": "Jack Holy"}],
                [{"first_name": "Jack", "full_name": "Jack Holy"}]
            ),
        ],
        ids=[
            "First name is None",
            "No first name at all"
        ]
    )
    def test_restore_names(self, users: list, expected_data: list) -> None:
        users_copy = copy.deepcopy(users)
        restore_names.restore_names(users_copy)
        assert users_copy == expected_data
