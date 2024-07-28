import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_dict, output_dict",
    [
        pytest.param(
            [{
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }],
            [{
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }],
            id="should return first name when first name is empty"
        ),
        pytest.param(
            [{
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }],
            [{
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }],
            id="should return first name when no first name in dict"
        )
    ]
)
def test_restore_names(input_dict: dict, output_dict: dict) -> None:
    dict_to_change = input_dict
    restore_names(dict_to_change)
    assert input_dict == output_dict
