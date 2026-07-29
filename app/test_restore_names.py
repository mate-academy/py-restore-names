import pytest
from app.restore_names import restore_names


@pytest.fixture()
def template_fixed_users_list() -> list:
    fixed_users = [
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
    return fixed_users


@pytest.fixture()
def template_not_fixed_users_list() -> list:
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


def test_restore_names(template_fixed_users_list: list,
                       template_not_fixed_users_list: list) -> None:

    restore_names(template_not_fixed_users_list)

    assert template_fixed_users_list == template_not_fixed_users_list
