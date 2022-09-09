import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_with_no_first_name():
    yield {
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }


@pytest.fixture()
def user_with_first_name_equals_none():
    yield {
        "first_name": None,
        "last_name": "Adams",
        "full_name": "Mike Adams",
    }


def test_should_create_first_name_when_key_is_missing(user_with_no_first_name):
    restore_names([user_with_no_first_name])
    assert user_with_no_first_name["first_name"] == "Jack"


def test_should_fill_none_first_name(user_with_first_name_equals_none):
    restore_names([user_with_first_name_equals_none])
    assert user_with_first_name_equals_none["first_name"] == "Mike"
