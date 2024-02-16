import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "initial_data, expected_result",
        [
            pytest.param(
                [{
                    "first_name": None,
                    "full_name": "Jack Holy"
                }],
                [{
                    "first_name": "Jack",
                    "full_name": "Jack Holy"
                }],
                id="should replace first name from full name"
            ),
            pytest.param(
                [{
                    "full_name": "Mike Adams"
                }],
                [{
                    "first_name": "Mike",
                    "full_name": "Mike Adams"
                }],
                id="should create first name from full name"
            )
        ]
    )
    def test_modify_correctly(
            self,
            initial_data: list,
            expected_result: list
    ) -> None:
        restore_names(initial_data)
        assert initial_data == expected_result
