import pytest
from app.restore_names import restore_names


@pytest.fixture
def user_template_none() -> dict:
    return {
        "first_name": None,
        "last_name": "Shevchenko",
        "full_name": "Taras Shevchenko"
    }


@pytest.fixture
def user_template_without_first_name() -> dict:
    return {
        "last_name": "Shevchenko",
        "full_name": "Taras Shevchenko"
    }


@pytest.fixture
def user_template_full() -> dict:
    return {
        "first_name": "Taras",
        "last_name": "Shevchenko",
        "full_name": "Taras Shevchenko"
    }


def test_restore_first_name_none(user_template_none: dict) -> None:
    users = [user_template_none]
    restore_names(users)
    assert users == [
        {
            "first_name": "Taras",
            "last_name": "Shevchenko",
            "full_name": "Taras Shevchenko"
        }
    ]


def test_restore_no_first_name(user_template_without_first_name: dict) -> None:
    users = [user_template_without_first_name]
    restore_names(users)
    assert users == [
        {
            "first_name": "Taras",
            "last_name": "Shevchenko",
            "full_name": "Taras Shevchenko"
        }
    ]


def test_restore_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_full_name(user_template_full: dict) -> None:
    users = [user_template_full]
    restore_names(users)
    assert users == [
        {
            "first_name": "Taras",
            "last_name": "Shevchenko",
            "full_name": "Taras Shevchenko"
        }
    ]
