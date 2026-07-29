import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_data() -> list:
    yield [
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


@pytest.fixture()
def user_data_with_none() -> list:
    yield [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


@pytest.fixture()
def user_data_missing_firstname() -> list:
    yield [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_first_name_with_none(
    user_data: list,
    user_data_with_none: list
) -> None:
    restore_names(user_data_with_none)
    assert user_data_with_none == user_data


def test_first_name_missing(
    user_data: list,
    user_data_missing_firstname: list
) -> None:
    restore_names(user_data_missing_firstname)
    assert user_data_missing_firstname == user_data
