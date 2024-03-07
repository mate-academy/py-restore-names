import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> list:
    users = [
        {"last_name": "Holy", "full_name": "Jack Holy", },
        {"last_name": "Adams", "full_name": "Mike Adams", },
    ]
    return users


def test_if_first_name_is_not_exist(users_template: list) -> None:
    restore_names(users_template)
    assert users_template[0]["first_name"] == "Jack"
    assert users_template[1]["first_name"] == "Mike"


def test_if_first_name_is_none(users_template: list) -> None:
    users_template[0]["first_name"] = None
    users_template[1]["first_name"] = None
    restore_names(users_template)
    assert users_template[0]["first_name"] == "Jack"
    assert users_template[1]["first_name"] == "Mike"
