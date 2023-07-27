import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_w_missing_1st_name() -> list:
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
def test_and_add_first_name(user_w_missing_1st_name):
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


def test_restore_names_with_missing_first_name(user_w_missing_1st_name):
    restore_names(user_w_missing_1st_name)
    assert user_w_missing_1st_name[0]["first_name"] == "Jack"
    assert user_w_missing_1st_name[1]["first_name"] == "Mike"


# Test case for users with existing first_name
def test_restore_names_with_existing_first_name(test_and_add_first_name):
    restore_names(test_and_add_first_name)
    assert test_and_add_first_name[0]["first_name"] == "Jack"
    assert test_and_add_first_name[1]["first_name"] == "Mike"
