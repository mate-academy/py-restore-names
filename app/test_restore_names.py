import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "checked_list, result",
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
            id="function should restore first_name with None"
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
            id="function should restore dict without 'first_name' key"
        ),
    ]
)
def test_return_restored_first_name(
        checked_list: list[dict],
        result: list[dict]) -> None:
    restore_names(checked_list)
    assert checked_list == result
