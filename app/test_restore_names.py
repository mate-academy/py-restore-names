import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> [dict]:
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


def test_should_return_none(users_template: [dict]) -> None:
    assert restore_names(users=users_template) is None


def test_should_add_first_name_when_it_is_missing(
        users_template: [dict]) -> None:
    assert ("first_name" not in users_template[1].keys()) is True
    restore_names(users=users_template)
    assert users_template[1]["first_name"] == "Mike"


def test_should_add_first_name_when_it_is_none(users_template: [dict]) -> None:
    restore_names(users=users_template)
    assert users_template[0]["first_name"] == "Jack"
