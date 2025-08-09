import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("corrupted_user_dict,fixed_user_dict", [
    pytest.param(
        [{"first_name": "John",
          "last_name": "Smith",
          "full_name": "John Smith"}],
        [{"first_name": "John",
          "last_name": "Smith",
          "full_name": "John Smith"}],
        id="test everything is correct, function does nothing"
    ),
    pytest.param(
        [{"first_name": None,
          "last_name": "Holy",
          "full_name": "Jack Holy"}],
        [{"first_name": "Jack",
          "last_name": "Holy",
          "full_name": "Jack Holy"}],
        id="test first name is none, function fixes it"
    ),
    pytest.param(
        [{"last_name": "Adams",
          "full_name": "Mike Adams"}],
        [{"first_name": "Mike",
          "last_name": "Adams",
          "full_name": "Mike Adams"}],
        id="test no first name, function adds it"
    )
])
def test_user(corrupted_user_dict: dict, fixed_user_dict: dict) -> None:
    restore_names(corrupted_user_dict)
    assert corrupted_user_dict == fixed_user_dict
