import pytest

from app.restore_names import restore_names


@pytest.fixture()
def user_initials() -> list[dict]:
    return [{
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }]


def test_correct_restoring_of_the_name_with_first_name_eq_none(
        user_initials: list[dict]) -> None:
    restore_names(user_initials)
    first_name_taken_from_fullname = user_initials[0]["full_name"].split()[0]
    assert user_initials[0]["first_name"] == first_name_taken_from_fullname


def test_correct_restoring_of_the_name_with_missing_first_name(
        user_initials: list[dict]) -> None:
    del user_initials[0]["first_name"]
    restore_names(user_initials)
    first_name_taken_from_fullname = user_initials[0]["full_name"].split()[0]
    assert user_initials[0]["first_name"] == first_name_taken_from_fullname
