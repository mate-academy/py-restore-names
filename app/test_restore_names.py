import pytest
from app.restore_names import restore_names
from typing import List
from unittest.mock import MagicMock


@pytest.fixture
def database_fixture() -> List[dict]:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]


def test_function_should_return_none(
        database_fixture: MagicMock
) -> None:
    assert restore_names(database_fixture) is None


def test_should_add_missing_names(
        database_fixture: MagicMock
) -> None:
    restore_names(database_fixture)
    assert database_fixture[0]["first_name"] == "Jack"
    assert database_fixture[1]["first_name"] == "Mike"
