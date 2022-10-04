import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_list_template():
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
def expected_user_list():
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


def test_should_not_return_anything(user_list_template):
    assert restore_names(user_list_template) is None


def test_should_restore_first_name_if_user_doesnt_have_it_or_it_is_none(
        user_list_template,
        expected_user_list
):
    restore_names(user_list_template)
    assert user_list_template == expected_user_list
