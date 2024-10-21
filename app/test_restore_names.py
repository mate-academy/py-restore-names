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


def test_restore_none_name(users_template: list) -> None:
    restore_names(users_template)
    user = users_template[0]
    assert user["first_name"] == "Jack"


def test_restore_no_name(users_template: list) -> None:
    user = users_template[0]
    del user["first_name"]
    restore_names(users_template)
    assert user["first_name"] == "Jack"
