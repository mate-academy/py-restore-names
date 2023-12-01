import pytest
from typing import List
from app.restore_names import restore_names


class TestRestoreNames:

    @pytest.mark.parametrize(
        "input_data,expected_output",
        [
            (
                    [{
                        "first_name": None,
                        "last_name": "Holy",
                        "full_name": "Jack Holy"
                    }],
                    [{
                        "first_name": "Jack",
                        "last_name": "Holy",
                        "full_name": "Jack Holy"
                    }]
            ),
            (
                    [{
                        "last_name": "Adams",
                        "full_name": "Mike Adams"
                    }],
                    [{
                        "first_name": "Mike",
                        "last_name": "Adams",
                        "full_name": "Mike Adams"
                    }]

            ),
            (
                    [{
                        "first_name": "Jack",
                        "last_name": "Holy",
                        "full_name": "Jack Holy"
                    }],
                    [{
                        "first_name": "Jack",
                        "last_name": "Holy",
                        "full_name": "Jack Holy"
                    }]
            )
        ],
        ids=[
            "Test case where the first name is None",
            "Test case where the first name is not present",
            "Test case where the first name is already present"
        ]
    )
    def test_restore_names(
        self,
        input_data: List[dict],
        expected_output: List[dict]
    ) -> None:
        restore_names(input_data)
        assert input_data == expected_output
