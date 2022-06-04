import pytest
from app.restore_names import restore_names


class TestRestoreNames:

    @pytest.mark.parametrize(
        "users_data, restored_data",
        [
            pytest.param(
                [{"first_name": None,
                  "last_name": "Holy",
                  "full_name": "Jack Holy"}],
                [{"first_name": "Jack",
                  "last_name": "Holy",
                  "full_name": "Jack Holy"}],
                id="first_name shouldn't be None"
            ),
            pytest.param(
                [{"last_name": "Adams",
                  "full_name": "Mike Adams"}],
                [{"first_name": "Mike",
                  "last_name": "Adams",
                  "full_name": "Mike Adams"}],
                id="user should have first name restored"
            )
        ]
    )
    def test_restore_name(self,
                          users_data,
                          restored_data):
        user = users_data
        restore_names(user)
        assert user == restored_data

