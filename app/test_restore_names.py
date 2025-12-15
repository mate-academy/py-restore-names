import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "users_in, users_out",
        [
            pytest.param(
                [
                    {
                        "first_name": None,
                        "last_name": "Holy",
                        "full_name": "Jack Holy"
                    }
                ],
                [
                    {
                        "first_name": "Jack",
                        "last_name": "Holy",
                        "full_name": "Jack Holy",
                    }
                ],
                id="test: first_name = None"
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
                id="test: first_name missing"
            )
        ]
    )
    def test_restore_names(
            self,
            users_in,
            users_out
    ):
        restore_names(users_in)
        assert users_in == users_out
