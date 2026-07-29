import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_data() -> list:
    return [
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


@pytest.fixture()
def user_data_restored() -> list:
    return [
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


def test_first_name_correction(user_data: list,
                               user_data_restored: list) -> None:
    restore_names(user_data)
    assert user_data == user_data_restored
