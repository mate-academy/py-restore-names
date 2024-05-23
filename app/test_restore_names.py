import pytest
from app.restore_names import restore_names


@pytest.fixture
def data() -> tuple:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": None,
            "last_name": "Daniels",
            "full_name": "Jack Daniels",
        },
    ]
    expected = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Jack",
            "last_name": "Daniels",
            "full_name": "Jack Daniels",
        },
    ]
    yield users, expected


def test_data(data: tuple) -> None:
    users, expected = data
    restore_names(users)
    assert users == expected
