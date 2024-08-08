import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_dict() -> dict:
    data = {
        "data_before_restoring": [
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
        "data_after_restoring": [
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
        ],
    }
    return data


def test_restore_names(users_dict: dict) -> None:
    users = users_dict["data_before_restoring"]
    restore_names(users)
    assert users == users_dict["data_after_restoring"]
