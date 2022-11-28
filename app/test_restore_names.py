import pytest

from app.restore_names import restore_names


@pytest.fixture()
def user_1() -> list[dict]:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


@pytest.fixture()
def user_2() -> list[dict]:
    return [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_when_first_name_is_none(user_1: list[dict]) -> None:

    restore_names(user_1)

    restore_names_user = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    assert user_1 == restore_names_user


def test_when_first_name_is_absent(user_2: list[dict]) -> None:

    restore_names(user_2)

    restore_names_user = [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    assert user_2 == restore_names_user
