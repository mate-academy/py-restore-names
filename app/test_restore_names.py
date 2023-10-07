import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "inputs, output",
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
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy"},
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                }
            ]
        )
    ]
)
def test_restore_names(inputs: list, output: list) -> None:
    restore_names(inputs)
    assert inputs == output
