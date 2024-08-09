import pytest
from app.restore_names import restore_names


@pytest.fixture()
def initial_dict() -> list:
    yield [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"}
    ]


@pytest.fixture()
def result_dict() -> list:
    yield [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"}
    ]


def test_should_fulfill_name_if_it_was_none(initial_dict: list,
                                            result_dict: list) -> None:
    restore_names(initial_dict)
    assert initial_dict == result_dict
