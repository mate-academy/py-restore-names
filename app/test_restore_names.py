import pytest
import copy
from app.restore_names import restore_names


@pytest.fixture
def user_template() -> list:
    return [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


@pytest.fixture
def another_user_template(user_template: list) -> list:
    return copy.deepcopy(user_template)


def test_should_do_nothing_if_correct(user_template: list,
                                      another_user_template: list
                                      ) -> None:
    restore_names(user_template)
    assert user_template == another_user_template


def test_should_add_name_if_none(user_template: list,
                                 another_user_template: list
                                 ) -> None:
    user_template[0]["first_name"] = None
    restore_names(user_template)
    assert user_template == another_user_template


def test_should_add_name_if_key_not_exist(user_template: list,
                                          another_user_template: list
                                          ) -> None:
    del (user_template[0]["first_name"])
    restore_names(user_template)
    assert user_template == another_user_template
