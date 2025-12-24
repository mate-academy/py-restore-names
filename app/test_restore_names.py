import pytest
from app.restore_names import restore_names


@pytest.fixture()
def create_wrong_data_base() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    return users


def test_correct_work_of_func(create_wrong_data_base: list) -> None:
    restore_names(create_wrong_data_base)
    for user in create_wrong_data_base:
        assert "first_name" in user
        assert user["first_name"] == user["full_name"].split()[0]
