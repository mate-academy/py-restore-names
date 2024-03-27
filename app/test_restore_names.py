import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    return users


def test_user_first_name_equal_none(user_template: pytest.fixture) -> None:
    restore_names(user_template)
    assert user_template[0] == {
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }


def test_user_first_name_doesnt_exist(user_template: pytest.fixture) -> None:
    restore_names(user_template)
    assert user_template[1] == {
        "first_name": "Mike",
        "last_name": "Adams",
        "full_name": "Mike Adams", }
