import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_list() -> list:
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


def test_should_restore_firstname_if_it_is_none_or_absent(
        users_list: list
) -> None:
    restore_names(users_list)
    assert users_list[0]["first_name"] == "Jack"
    assert users_list[1]["first_name"] == "Mike"
