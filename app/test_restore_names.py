import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> list:
    return [{
        "last_name": "Adams",
        "full_name": "Mike Adams",
    }]


def test_without_key_first_name(users_template: object) -> None:
    restore_names(users_template)

    assert users_template[0] == {
        "first_name": "Mike",
        "last_name": "Adams",
        "full_name": "Mike Adams",
    }


def test_wit_first_name_none(users_template: object) -> None:
    users_template[0]["first_name"] = None
    restore_names(users_template)

    assert users_template[0] == {
        "first_name": "Mike",
        "last_name": "Adams",
        "full_name": "Mike Adams",
    }
