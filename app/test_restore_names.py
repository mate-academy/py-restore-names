import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        (
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
        )
    ]
)
def test_restore_names_valid_inputs(
        input_list: list,
        expected_output: list
) -> None:
    restore_names(input_list)
    assert input_list == expected_output
