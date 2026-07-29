import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user_dict, result",
    [
        pytest.param([{"last_name": "Adams", "full_name": "Mike Adams"}],
                     [{"first_name": "Mike", "last_name": "Adams",
                       "full_name": "Mike Adams"}],
                     id="test_no_key_first_name"),
        pytest.param([{"first_name": None, "last_name": "Adams",
                       "full_name": "Mike Adams"}],
                     [{"first_name": "Mike", "last_name": "Adams",
                       "full_name": "Mike Adams"}],
                     id="test_first_name_None"),
    ]
)
def test_restore_name(user_dict: list[dict], result: list[dict]) -> None:
    restore_names(user_dict)
    assert user_dict == result
