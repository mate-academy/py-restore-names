import pytest
from app.restore_names import restore_names


@pytest.fixture()
def test_user() -> list:
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


@pytest.fixture()
def test_user_result() -> list:
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


def test_restore_names(test_user: list[dict],
                       test_user_result: list[dict]) -> None:
    restore_names(test_user)
    assert test_user == test_user_result
