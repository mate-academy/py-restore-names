import pytest
from app.restore_names import restore_names


@pytest.fixture
def user_with_none_first_name() -> dict:
    return {
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }


@pytest.fixture
def user_without_first_name_key() -> dict:
    return {
        "last_name": "Adams",
        "full_name": "Mike Adams",
    }


@pytest.fixture
def user_with_first_name() -> dict:
    return {
        "first_name": "John",
        "last_name": "Doe",
        "full_name": "John Doe",
    }


def test_restores_when_first_name_is_none(
    user_with_none_first_name: dict,
) -> None:
    restore_names([user_with_none_first_name])
    assert user_with_none_first_name["first_name"] == "Jack"


def test_restores_when_first_name_key_is_missing(
    user_without_first_name_key: dict,
) -> None:
    restore_names([user_without_first_name_key])
    assert user_without_first_name_key["first_name"] == "Mike"


def test_does_not_overwrite_existing_first_name(
    user_with_first_name: dict,
) -> None:
    restore_names([user_with_first_name])
    assert user_with_first_name["first_name"] == "John"


def test_restores_multiple_users(
    user_with_none_first_name: dict,
    user_without_first_name_key: dict,
    user_with_first_name: dict,
) -> None:
    users = [
        user_with_none_first_name,
        user_without_first_name_key,
        user_with_first_name,
    ]
    restore_names(users)
    assert user_with_none_first_name["first_name"] == "Jack"
    assert user_without_first_name_key["first_name"] == "Mike"
    assert user_with_first_name["first_name"] == "John"


def test_returns_none(
    user_with_none_first_name: dict,
) -> None:
    result = restore_names([user_with_none_first_name])
    assert result is None


def test_empty_list_does_not_raise() -> None:
    restore_names([])
