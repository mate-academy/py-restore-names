import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> list:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_user_first_name_is_none(users_template: list) -> None:
    restore_names(users_template)
    assert users_template[0]["first_name"] == "Jack"


def test_user_first_name_is_missing(users_template: list) -> None:
    del users_template[0]["first_name"]
    restore_names(users_template)
    assert users_template[0]["first_name"] == "Jack"
