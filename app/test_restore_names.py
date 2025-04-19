import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_input,users_output",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Black",
                    "full_name": "John Black"
                },
                {
                    "first_name": "Bob",
                    "last_name": "White",
                    "full_name": "Bob White"
                }
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Black",
                    "full_name": "John Black"
                },
                {
                    "first_name": "Bob",
                    "last_name": "White",
                    "full_name": "Bob White"
                }
            ]
        ),
        (
            [
                {
                    "last_name": "Smith",
                    "full_name": "Adam Smith"
                }
            ],
            [
                {
                    "first_name": "Adam",
                    "last_name": "Smith",
                    "full_name": "Adam Smith"
                },
            ]
        )
    ]
)
def test_function_returns_correct_first_name(
        users_input: list,
        users_output: list
) -> None:
    restore_names(users_input)
    assert users_input == users_output
