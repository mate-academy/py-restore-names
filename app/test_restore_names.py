import pytest
from _pytest.mark import ParameterSet

from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "input_user, output_user",
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
                id="Should change users whose first_name is equal to None"
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
                id="Should change users whose first_name is missing"

            )
        ]
    )
    def test_change_first_name(
        self,
        input_user: ParameterSet,
        output_user: ParameterSet
    ) -> None:
        user = input_user
        restore_names(user)
        assert user == output_user
