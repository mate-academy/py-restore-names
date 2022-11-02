import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user() -> list:
    return [
        {"first_name": None,
         "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"last_name": "Adams",
         "full_name": "Mike Adams"},
    ]


def test_should_no_return(user) -> None:
    assert restore_names(user) is None


def test_should_return_user_name_when_it_is_none(user) -> None:
    restore_names(user)
    assert (user[0]["first_name"]
            == user[0]["full_name"].split()[0])


def test_should_return_user_name_when_no_exist(user) -> None:
    restore_names(user)
    assert (user[1]["first_name"]
            == user[1]["full_name"].split()[0])


def test_should_do_nothing_if_user_name_exist(user) -> None:
    user[0]["first_name"] = "Dave"
    restore_names(user)
    assert user[0]["first_name"] == "Dave"
