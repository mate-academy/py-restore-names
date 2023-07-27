import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_w_missing_1st_name() -> list[dict]:
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
def user_w_current_1st_name(user_w_missing_1st_name: list[dict]) -> list[dict]:
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


def test_restore_names_with_missing_first_name(
        user_w_missing_1st_name: list[dict]) -> None:
    restore_names(user_w_missing_1st_name)
    assert user_w_missing_1st_name[0]["first_name"] == "Jack"
    assert user_w_missing_1st_name[1]["first_name"] == "Mike"


# Test case for users with existing first_name
def test_restore_names_with_existing_first_name(
        user_w_current_1st_name: list[dict]) -> None:
    restore_names(user_w_current_1st_name)
    assert user_w_current_1st_name[0]["first_name"] == "Jack"
    assert user_w_current_1st_name[1]["first_name"] == "Mike"
