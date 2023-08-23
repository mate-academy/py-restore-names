import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_without_first_name_value() -> dict:
    return {
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }


@pytest.fixture()
def user_without_first_name_field() -> dict:
    return {
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }


def test_user_without_first_name_value(
        user_without_first_name_value: dict
) -> None:
    restore_names([user_without_first_name_value])
    assert user_without_first_name_value["first_name"] == "Jack"


def test_user_without_first_name_field(
        user_without_first_name_field: dict
) -> None:
    restore_names([user_without_first_name_field])
    assert user_without_first_name_field["first_name"] == "Jack"
