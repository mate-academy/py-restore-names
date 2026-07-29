import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_data_with_none_value() -> list:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]


@pytest.fixture()
def users_data_with_no_key() -> list:
    return [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_first_name_key_creation_when_no_key(
        users_data_with_no_key: list
) -> None:
    restore_names(users_data_with_no_key)
    assert users_data_with_no_key == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_first_name_key_creation_when_value_is_none(
        users_data_with_none_value: list
) -> None:
    restore_names(users_data_with_none_value)
    assert users_data_with_none_value == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]
