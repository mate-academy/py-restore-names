import pytest
from app.restore_names import restore_names


@pytest.fixture()
def correct_user() -> list:
    yield [{
        "first_name": "Mike",
        "last_name": "Adams",
        "full_name": "Mike Adams"
    }]


@pytest.fixture()
def user_with_none_name() -> list:
    yield [{
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }]


@pytest.fixture()
def user_without_first_name() -> list:
    yield [{
        "last_name": "Adams",
        "full_name": "Lily Adams"
    }]


def test_func_when_all_data_is_correct(correct_user) -> None:
    restore_names(correct_user)
    assert correct_user[0]["first_name"] == "Mike"


def test_func_when_first_name_is_none(user_with_none_name) -> None:
    restore_names(user_with_none_name)
    assert user_with_none_name[0]["first_name"] == "Jack"


def test_func_when_first_name_is_absent(user_without_first_name) -> None:
    restore_names(user_without_first_name)
    assert user_without_first_name[0]["first_name"] == "Lily"
