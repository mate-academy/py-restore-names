import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> list[dict]:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_restore_names_none(users_template: [dict]) -> None:
    restore_names(users_template)
    user = users_template[0]
    assert user["first_name"] == "Jack"


def test_restore_name_does_not_exist(users_template: [dict]) -> None:
    user = users_template[0]
    del user["first_name"]
    restore_names(users_template)
    assert user["first_name"] == "Jack"
