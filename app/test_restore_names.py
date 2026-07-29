import pytest
from app.restore_names import restore_names


@pytest.fixture()
def damaged_data() -> list:
    return [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"}
    ]


@pytest.fixture()
def undamaged_data() -> list:
    return [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_restore_names(damaged_data: list, undamaged_data: list) -> None:
    restore_names(damaged_data)
    assert damaged_data == undamaged_data
