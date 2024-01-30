import pytest
from app.restore_names import restore_names


@pytest.fixture
def user_if_something_wrong() -> list[dict]:
    return [
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
def correct_list() -> list[dict]:
    return [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_restore_names(
    user_if_something_wrong: callable,
    correct_list: callable
) -> None:
    restore_names(user_if_something_wrong)
    assert user_if_something_wrong == correct_list
