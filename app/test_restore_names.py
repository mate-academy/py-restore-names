import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_fixture_first_name_is_none() -> None:
    return [
        {
            "first_name": None,
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


@pytest.fixture()
def user_fixture_first_name_doesnot_exists() -> None:
    return [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_restore_name_first_name_is_none(
        user_fixture_first_name_is_none: list[dict]) -> None:

    restore_names(user_fixture_first_name_is_none)
    assert user_fixture_first_name_is_none == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_restore_name_first_name_doesnot_exists(
        user_fixture_first_name_doesnot_exists: list[dict],) -> None:

    restore_names(user_fixture_first_name_doesnot_exists)
    assert user_fixture_first_name_doesnot_exists == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]
