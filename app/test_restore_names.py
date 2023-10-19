import pytest

from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_first_name_is_none(user_template: list) -> None:
    restore_names(user_template)
    assert (
        user_template[0].get("first_name") == "Jack"
    )


def test_first_name_empty(user_template: list) -> None:
    restore_names(user_template)
    assert (
        user_template[1].get("first_name") == "Mike"
    )


def test_first_name_not_field(user_template: list) -> None:
    restore_names(user_template)
    assert (
        user_template[2] == {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    )


def test_function_return_none(user_template: list) -> None:
    restore_names(user_template)
    assert (restore_names(user_template) is None)
