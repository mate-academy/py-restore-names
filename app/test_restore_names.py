import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list:
    users == [
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


def test_function_returns_none(user_template: list) -> None:
    assert restore_names(user_template) is None


def test_function_restore_names(user_template: list) -> None:
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Jake"
    assert user_template[1]["first_name"] == "Mike"
