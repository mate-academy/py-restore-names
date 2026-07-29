import pytest
from app.restore_names import restore_names


@pytest.fixture
def first_name_is_none() -> list:
    user = [{
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }]
    return user


@pytest.fixture
def first_name_is_empty() -> list:
    user = [{
        "last_name": "Adams",
        "full_name": "Mike Adams",
    }]
    return user


def test_first_name_is_none(first_name_is_none: list) -> None:
    restore_names(first_name_is_none)
    assert first_name_is_none[0]["first_name"] == "Jack"


def test_first_name_is_empty(first_name_is_empty: list) -> None:
    restore_names(first_name_is_empty)
    assert first_name_is_empty[0]["first_name"] == "Mike"
