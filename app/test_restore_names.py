import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list:
    return [
        {"first_name": None,
         "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"last_name": "Adams",
         "full_name": "Mike Adams"},
    ]


def test_should_no_return(user_template: list) -> None:
    assert restore_names(user_template) is None


def test_should_return_user_name_when_it_is_none(user_template: list) -> None:
    restore_names(user_template)
    assert (user_template[0]["first_name"]
            == user_template[0]["full_name"].split()[0])


def test_should_return_user_name_when_no_exist(user_template: list) -> None:
    restore_names(user_template)
    assert (user_template[1]["first_name"]
            == user_template[1]["full_name"].split()[0])


def test_should_do_nothing_if_user_name_exist(user_template: list) -> None:
    user_template[0]["first_name"] = "Dave"
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Dave"
