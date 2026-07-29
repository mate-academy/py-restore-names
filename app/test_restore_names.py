import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "wrong_users_data,fixed_users_data",
        [
            pytest.param(
                [
                    {
                        "first_name": None,
                        "last_name": "Holy",
                        "full_name": "Jack Holy",
                    }
                ],
                [
                    {
                        "first_name": "Jack",
                        "last_name": "Holy",
                        "full_name": "Jack Holy",
                    }
                ],
                id="first name is none"
            ),

            pytest.param(
                [
                    {
                        "last_name": "Adams",
                        "full_name": "Mike Adams",
                    }
                ],

                [
                    {
                        "first_name": "Mike",
                        "last_name": "Adams",
                        "full_name": "Mike Adams",
                    }
                ],
                id="first name not exist"
            )
        ]
    )
    def test_first_name_restored(
            self,
            wrong_users_data,
            fixed_users_data
    ):
        restore_names(wrong_users_data)
        assert wrong_users_data == fixed_users_data
