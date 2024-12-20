import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_dict,expected_dict",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }
        ),
        (
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            {
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }
        )
    ]
)
def test_should_fix_dict(
        input_dict: list[dict],
        expected_dict: dict
) -> None:
    restore_names(input_dict)
    assert input_dict[0] == expected_dict
