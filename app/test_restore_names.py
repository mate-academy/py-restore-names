import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "corrupted_dict,expected_fixed_dict",
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
                },
            ]
        )
    ]
)
def test_check_if_function_fixing_lost_first_name_correctly(
        corrupted_dict: list,
        expected_fixed_dict: list
) -> None:
    restore_names(corrupted_dict)
    assert (
        corrupted_dict[0]["first_name"] == expected_fixed_dict[0]["first_name"]
    )
    assert (
        corrupted_dict[1]["first_name"] == expected_fixed_dict[1]["first_name"]
    )
