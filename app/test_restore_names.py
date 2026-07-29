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


def test_should_change_first_name_if_its_none(users_template: list) -> None:
    restore_names(users_template)
    assert users_template[0]["first_name"] == "Jack"


def test_should_create_first_name_if_its_not_existed(
        users_template: list
) -> None:
    del users_template[0]["first_name"]
    restore_names(users_template)
    assert users_template[0]["first_name"] == "Jack"


def test_should_return_none(users_template: list) -> None:
    assert restore_names(users_template) is None
