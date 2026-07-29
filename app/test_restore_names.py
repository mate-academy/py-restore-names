import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> list:
    return [{"first_name": None,
             "last_name": "Johnson",
             "full_name": "John Johnson"}]


def test_restore_name_if_none(users_template: list) -> None:
    restore_names(users_template)
    assert users_template == [{"first_name": "John",
                               "last_name": "Johnson",
                               "full_name": "John Johnson"}]


def test_restore_name_if_not_exist(users_template: list) -> None:
    del users_template[0]["first_name"]
    restore_names(users_template)
    assert users_template == [{"first_name": "John",
                               "last_name": "Johnson",
                               "full_name": "John Johnson"}]
