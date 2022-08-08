import pytest
from app.restore_names import restore_names


# update progress
class TestRestoreNames:
    @pytest.mark.parametrize(
        "initial_list, expected_list",
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
                id="should insert name from 'full_name' "
                   "to 'first_name' when 'first_name' is None"
            ),

            pytest.param(
                [
                    {
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
                id="should insert name from 'full_name' "
                   "to 'first_name' when 'first_name' not in dict"
            )

        ]
    )
    def test_should_return_correct_first_name(
            self,
            initial_list,
            expected_list
    ):
        restore_names(initial_list)
        assert initial_list == expected_list
