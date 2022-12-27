import pytest
from app.restore_names import restore_names


@pytest.fixture
def user_damaged() -> list:
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
def user_revised() -> list:
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
        },
    ]


def test_names_are_restored_properly(
        user_damaged: list,
        user_revised: list
) -> None:
    restore_names(user_damaged)
    assert user_damaged == user_revised
