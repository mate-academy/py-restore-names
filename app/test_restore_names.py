import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users() -> list:
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
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": None,
            "last_name": "Jeager",
            "full_name": "Grisha Jeager",
        },
        {
            "last_name": "Smith",
            "full_name": "Adam Smith",
        },
    ]


@pytest.fixture()
def correct_users() -> list:
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
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Grisha",
            "last_name": "Jeager",
            "full_name": "Grisha Jeager",
        },
        {
            "first_name": "Adam",
            "last_name": "Smith",
            "full_name": "Adam Smith",
        },
    ]


def test_correct_values(users, correct_users):
    restore_names(users)
    assert users == correct_users


def test_no_change_if_first_name_exists(correct_users):
    expected_users = correct_users[:]
    restore_names(correct_users)
    assert correct_users == expected_users


def test_empty_list():
    users = []
    expected_users = []

    restore_names(users)
    assert users == expected_users
