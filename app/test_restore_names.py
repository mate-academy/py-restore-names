import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_list, result", [
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
            id="Test when key 'first_name' is None"),
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
            id="Test when input dictionary does not have key 'first_name'")
    ]
)
def test_restore_names(input_list: list[dict], result: list[dict]) -> None:
    restore_names(input_list)
    assert input_list == result
