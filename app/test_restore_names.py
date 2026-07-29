import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_list() -> None:
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


def test_restore_name(user_list: list) -> None:
    restore_names(user_list)
    assert user_list[0]["first_name"] == "Jack"
    assert user_list[1]["first_name"] == "Mike"
