

import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_info() -> list:
    info = [
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
    return info


def test_restore_name_functions(user_info: list) -> None:
    restore_names(user_info)
    assert user_info == [
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
