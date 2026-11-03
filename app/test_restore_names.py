import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_input, expected_output",
    [
        (
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
        ),
        (
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
        ),
        (
            [
                {
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "full_name": "Jane Doe",
                }
            ],
            [
                {
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "full_name": "Jane Doe",
                }
            ],
        ),
    ],
)
def test_restore_names(users_input: list, expected_output: list) -> None:
    result = restore_names(users_input)
    assert result is None
    assert users_input == expected_output
