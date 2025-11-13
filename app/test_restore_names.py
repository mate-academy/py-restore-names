import pytest
from app.restore_names import restore_names


@pytest.fixture(scope="function")
def user_template() -> list:
    users = [
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
    return users


def test_user_already_have_first_name(user_template: list) -> None:
    user_template[0]["first_name"] = "Jack"
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Jack"


def test_user_already_have_none_name(user_template: list) -> None:
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Jack"


def test_user_dont_have_name(user_template: list) -> None:
    restore_names(user_template)
    assert user_template[1]["first_name"] == "Mike"
