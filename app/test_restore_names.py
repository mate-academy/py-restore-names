import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_list, output_list",
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
                }
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
                }
            ]

        )
    ]
)
def test_should_set_correct_first_name(
    input_list: list[dict],
    output_list: list[dict]
) -> None:
    restore_names(input_list)
    assert input_list == output_list
