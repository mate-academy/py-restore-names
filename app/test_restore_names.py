import pytest
from app.restore_names import restore_names

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
]


@pytest.fixture
def func() -> None:
    yield restore_names(users)


def test_name_is_none(func: callable) -> None:
    assert users[0]["first_name"] == "Jack"


def test_name_absent(func: callable) -> None:
    assert users[1]["first_name"] == "Mike"
