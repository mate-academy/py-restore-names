import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list:
    return [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]


def test_user_does_not_have_first_name_or_none(user_template: list) -> None:
    restore_names(user_template)
    assert user_template == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_user_first_name_is_none(user_template: list) -> None:
    user_template[0]["first_name"] = None
    restore_names(user_template)
    assert user_template == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_func_does_not_return_anything(user_template: list) -> None:
    before_func = id(user_template[0])
    restore_names(user_template)
    after_func = id(user_template[0])
    assert before_func == after_func
