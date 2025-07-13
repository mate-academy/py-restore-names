import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_list() -> list:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


@pytest.fixture()
def users_list2() -> list:
    return [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


@pytest.fixture()
def users_list3() -> list:
    return [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy Junior",
        }
    ]


def test_first_name_is_none(users_list: list) -> None:
    restore_names(users_list)
    assert users_list[0]["first_name"] == "Jack"


def test_first_name_not_in_users(users_list2: list) -> None:
    restore_names(users_list2)
    assert users_list2[0]["first_name"] == "Jack"


def test_fullname_contain_extra_words(users_list3: list) -> None:
    restore_names(users_list3)
    assert users_list3[0]["first_name"] == "Jack"
