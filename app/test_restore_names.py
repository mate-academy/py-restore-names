import pytest
from app.restore_names import restore_names


@pytest.fixture(scope="function")
def users_wrong_template_to_check() -> list:
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


def test_check_is_first_name_exists(
        users_wrong_template_to_check: list
) -> None:
    restore_names(users_wrong_template_to_check)
    for user in users_wrong_template_to_check:
        assert "first_name" in user


def test_check_is_name_not_none(users_wrong_template_to_check: list) -> None:
    restore_names(users_wrong_template_to_check)
    for user in users_wrong_template_to_check:
        assert user["first_name"] is not None


def test_check_the_name_is_right(users_wrong_template_to_check: list) -> None:
    restore_names(users_wrong_template_to_check)
    for user in users_wrong_template_to_check:
        assert user["first_name"] == user["full_name"].split()[0]
