import pytest
from app.restore_names import restore_names


@pytest.fixture
def users() -> list[dict]:
    return [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }]


@pytest.fixture
def users_with_none() -> list[dict]:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }]


@pytest.fixture
def user_correct() -> list[dict]:
    return [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]


def test_restore_names_without_firs_name(users: list[dict],
                                         user_correct: list[dict]) -> None:
    restore_names(users)
    assert users == user_correct


def test_restore_whit_none_in_first_name(users_with_none: list[dict],
                                         user_correct: list[dict]) -> None:
    restore_names(users_with_none)
    assert users_with_none == user_correct
