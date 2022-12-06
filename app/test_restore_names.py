import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_datas() -> list:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    return users


def test_restore_name_func(users_datas: list) -> None:
    restore_names(users_datas)
    assert users_datas == [
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
    ]
