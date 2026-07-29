import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                },
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                },
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                },
            ],
        ),
        (
            [
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "John Doe"
                },
                {
                    "first_name": None,
                    "last_name": "Smith",
                    "full_name": "Samantha Smith",
                },
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "John Doe"
                },
                {
                    "first_name": "Samantha",
                    "last_name": "Smith",
                    "full_name": "Samantha Smith",
                },
            ],
        ),
    ],
)
def test_restore_names(
        input_data: list[dict],
        expected_data: list[dict]
) -> None:
    restore_names(input_data)
    assert (
        input_data == expected_data
    ), f"Expected {expected_data}, but got {input_data}"
