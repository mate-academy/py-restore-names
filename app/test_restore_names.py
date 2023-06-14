from copy import deepcopy
import pytest

from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> list[dict]:
    return [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_set_name_if_is_none_in_users(users_template: list[dict]) -> None:
    none_first_name_users = deepcopy(users_template)
    none_first_name_users[-1]["first_name"] = None

    restore_names(none_first_name_users)
    assert none_first_name_users == users_template


def test_set_name_if_users_with_no_name(users_template: list[dict]) -> None:
    no_first_name_users = deepcopy(users_template)

    del no_first_name_users[-1]["first_name"]
    restore_names(no_first_name_users)
    assert no_first_name_users == users_template


def test_the_list_must_be_the_same(users_template: list[dict]) -> None:
    list_id_before_restore = id(users_template)
    users_template[0]["first_name"] = None

    del users_template[-1]["first_name"]
    restore_names(users_template)
    assert id(users_template) == list_id_before_restore
