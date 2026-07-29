import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user() -> list[dict]:
    yield [
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
            "first_name": "Mark",
            "last_name": "Twain",
            "full_name": "Mark Twain",
        },
    ]


def test_correct_function(user: list[dict]) -> None:
    restore_names(user)
    assert user == [
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
            "first_name": "Mark",
            "last_name": "Twain",
            "full_name": "Mark Twain",
        },
    ]
