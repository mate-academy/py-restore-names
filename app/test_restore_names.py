import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user_dict, valid_first_name",
    [
        ({
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }, "Jack"),
        ({
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }, "Mike"),
        ({
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }, "Jack")
    ]
)
def test_restore_names(user_dict: dict, valid_first_name: str) -> None:
    restore_names([user_dict])
    assert user_dict["first_name"] == valid_first_name
