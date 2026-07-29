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
def without_first_name() -> list:
    user = [{
        "last_name": "Adams",
        "full_name": "Mike Adams",
    }]
    return user


def test_when_first_name_is_none(first_name_is_none: list) -> None:
    restore_names(first_name_is_none)
    assert first_name_is_none[0]["first_name"] == "Jack"


def test_when_without_first_name(without_first_name: list) -> None:
    restore_names(without_first_name)
    assert without_first_name[0]["first_name"] == "Mike"
