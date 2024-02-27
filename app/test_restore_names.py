import pytest
from app.restore_names import restore_names


@pytest.fixture(scope="function")
def user_template() -> list:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


@pytest.fixture(scope="function")
def another_user() -> list:
    return [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_restore_names_when_name_is_none(user_template: list) -> None:
    restore_names(user_template)

    assert user_template[0]["first_name"] == "Jack"


def test_restore_names_when_name_is_gap(another_user: list) -> None:
    restore_names(another_user)

    assert another_user[0]["first_name"] == "Jack"
