import pytest
from app.restore_names import restore_names


@pytest.fixture
def users() -> list:
    return [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"}
    ]


def test_restore_names(users) -> None:
    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Jack"
    assert users[3]["first_name"] == "Mike"


def test_restore_names_no_change(users) -> None:
    # Test if the function doesn't change the first_name if it's already correct
    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Jack"
    assert users[3]["first_name"] == "Mike"
