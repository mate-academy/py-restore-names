import pytest
from app.restore_names import restore_names
from typing import List


@pytest.mark.parametrize(
    "users_data, expected_data",
    [
        pytest.param(
            [
                {
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ],

            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ],
            id="with missing 'first_name' key"
        ),

        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ],

            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ],
            id="with one invalid dictionary"
        ),

        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },

                {
                    "first_name": None,
                    "last_name": "Moly",
                    "full_name": "Andrew Moly",
                },
            ],

            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },

                {
                    "first_name": "Andrew",
                    "last_name": "Moly",
                    "full_name": "Andrew Moly",
                },
            ],
            id="with two invalid dictionaries"
        ),

        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },

                {
                    "first_name": None,
                    "last_name": "Moly",
                    "full_name": "Andrew Moly",
                },

                {
                    "first_name": "Lili",
                    "last_name": "Poly",
                    "full_name": "Lili Poly",
                },

                {
                    "first_name": None,
                    "last_name": "Edison",
                    "full_name": "Paul Edison",
                },

                {
                    "first_name": None,
                    "last_name": "Frankfort",
                    "full_name": "Emilia Frankfort",
                },

                {
                    "first_name": "Andrew",
                    "last_name": "Fill",
                    "full_name": "Andrew Fill",
                },
            ],

            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },

                {
                    "first_name": "Andrew",
                    "last_name": "Moly",
                    "full_name": "Andrew Moly",
                },

                {
                    "first_name": "Lili",
                    "last_name": "Poly",
                    "full_name": "Lili Poly",
                },

                {
                    "first_name": "Paul",
                    "last_name": "Edison",
                    "full_name": "Paul Edison",
                },

                {
                    "first_name": "Emilia",
                    "last_name": "Frankfort",
                    "full_name": "Emilia Frankfort",
                },

                {
                    "first_name": "Andrew",
                    "last_name": "Fill",
                    "full_name": "Andrew Fill",
                },
            ],
            id="with six dictionaries"
        ),
    ]
)
def test_possible_options(
        users_data: List[dict],
        expected_data: List[dict]
) -> None:
    restore_names(users_data)
    assert users_data == expected_data
