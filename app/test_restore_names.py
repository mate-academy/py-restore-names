import pytest
from app.restore_names import restore_names

# flake8: noqa: ANN001
@pytest.fixture()
def some_fixture() -> None:
    pass


def test_restore_names_missing_first_name(some_fixture) -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Holy", "full_name": "Mike Adams"}
    ]
    restore_names(users)

    expected = [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Holy", "full_name": "Mike Adams"}
    ]

    assert users == expected
