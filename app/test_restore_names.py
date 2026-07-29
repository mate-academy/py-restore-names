import pytest
from app.restore_names import restore_names


@pytest.fixture
def in_dict() -> list:
    return [{
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy"}, {
        "last_name": "Adams",
        "full_name": "Mike Adams"}]


def test_restore_names(in_dict: list) -> None:
    restore_names(in_dict)
    assert in_dict == [{
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"},
        {"first_name": "Mike",
         "last_name": "Adams",
         "full_name": "Mike Adams"}]
