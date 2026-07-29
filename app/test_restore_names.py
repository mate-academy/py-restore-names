import pytest
from app.restore_names import restore_names


@pytest.fixture()
def first_name_is_none() -> list:
    user = [{"first_name": None,
             "last_name": "Smith",
             "full_name": "John Smith"
             }]
    return user


@pytest.fixture()
def without_name() -> list:
    user = [{"last_name": "Holy",
             "full_name": "Bob Holy",
             }]
    return user


def test_first_name_is_none(first_name_is_none: list) -> None:
    restore_names(first_name_is_none)
    assert first_name_is_none[0]["first_name"] == "John"


def test_without_first_name(without_name: list) -> None:
    restore_names(without_name)
    assert without_name[0]["first_name"] == "Bob"
