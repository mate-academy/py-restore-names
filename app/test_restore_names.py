import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template_none() -> list:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


@pytest.fixture()
def user_template_empty() -> list:
    return [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_restore_only_missing_names(user_template_none: list) -> None:
    restore_names(user_template_none)
    user = user_template_none[0]
    assert user["first_name"] == "Jack"


def test_restore_only_none_names(user_template_empty: list) -> None:
    restore_names(user_template_empty)
    user = user_template_empty[0]
    assert user["first_name"] == "Mike"
