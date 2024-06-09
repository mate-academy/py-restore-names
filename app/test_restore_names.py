import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_without_first_name() -> list:
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
def user_with_all_data() -> list:
    return [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_nme": "Mike Adams",
        },
    ]


@pytest.fixture
def user_empty() -> list:
    return []


def test_get_first_name_info(user_without_first_name: list) -> None:
    restore_names(user_without_first_name)
    expected = [
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
    assert user_without_first_name == expected


def test_user_has_all_data(user_with_all_data: list) -> None:
    restore_names(user_with_all_data)
    expected = [
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
    assert user_with_all_data == expected


def test_user_empty(user_empty: list) -> None:
    restore_names(user_empty)
    expected = []
    assert user_empty == expected
