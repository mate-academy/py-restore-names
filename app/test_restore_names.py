import pytest
from app.restore_names import restore_names


@pytest.fixture()
def income_user() -> list:
    user = [
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
    return user


@pytest.fixture()
def outcome_user() -> list:
    user = [
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
    return user


def test_restore_name_correctly(
    income_user: list,
    outcome_user: list
) -> None:
    restore_names(income_user)
    assert income_user == outcome_user
