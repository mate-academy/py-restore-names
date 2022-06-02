import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "initial_users,expected_users",
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
                id="Should add firstname when first name is None"
            ),
            pytest.param(
                [
                    {
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
                id="Should add firstname when first name doesnt exist"
            ),
        ]
    )
    def test_correct_change(
        self,
        initial_users,
        expected_users
    ):
        restore_names(initial_users)
        assert initial_users == expected_users
