import pytest
from main import restore_names


@pytest.fixture()
def list_before() -> list:
    return [
        {"first_name": None,
         "last_name": "Smith",
         "full_name": "John Smith"},
        {"first_name": None,
         "last_name": "Testovich",
         "full_name": "Test Testovich"}
    ]


def test_should_set_first_name_if_none(list_before: list) -> None:
    restore_names(list_before)
    assert list_before[0]["first_name"] == "John"
    assert list_before[1]["first_name"] == "Test"


def test_should_define_first_name_and_set(list_before: list) -> None:
    restore_names(list_before)
    assert list_before[0]["first_name"] == "John"
    assert list_before[1]["first_name"] == "Test"
