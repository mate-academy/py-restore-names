import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "users_incoming_list, users_out_list",
        [
            pytest.param(
                [
                    {
                        "first_name": None,
                        "last_name": "Holy",
                        "full_name": "Jack Holy",
                    },
                    {
                        "last_name": "Adams",
                        "full_name": "Mike Adams",
                    },
                ],
                [
                    {
                        "first_name": "Jack",
                        "last_name": "Holy",
                        "full_name": "Jack Holy",
                    },
                    {
                        "first_name": "Mike",
                        "last_name": "Adams",
                        "full_name": "Mike Adams",
                    },
                ],
                id="should return correct first name"
            ),
            pytest.param(
                [
                    {
                        "first_name": None,
                        "full_name": "Jack Holy",
                    }
                ],
                [
                    {
                        "first_name": "Jack",
                        "full_name": "Jack Holy",
                    }
                ],
                id="should return correct first name without last name"
            )
        ]
    )
    def test_restore_names_correctly(
            self,
            users_incoming_list,
            users_out_list
    ):
        restore_names(users_incoming_list)
        assert users_incoming_list == users_out_list
