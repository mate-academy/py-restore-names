import pytest
from app.restore_names import restore_names


@pytest.fixture()
def list_with_none() -> list:
    return [
        {"first_name": None,
         "last_name": "Smith",
         "full_name": "John Smith"},
        {"first_name": None,
         "last_name": "Testovich",
         "full_name": "Test Testovich"}
    ]


@pytest.fixture()
def list_with_empty() -> list:
    return [
        {"last_name": "Smith",
         "full_name": "John Smith"},
        {"last_name": "Testovich",
         "full_name": "Test Testovich"}
    ]


def test_should_set_first_name_if_none(list_with_none: list) -> None:
    restore_names(list_with_none)
    assert list_with_none[0]["first_name"] == "John"
    assert list_with_none[1]["first_name"] == "Test"


def test_should_define_first_name_and_set(list_with_empty: list) -> None:
    restore_names(list_with_empty)
    assert list_with_empty[0]["first_name"] == "John"
    assert list_with_empty[1]["first_name"] == "Test"
