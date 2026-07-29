import pytest
from app.restore_names import restore_names


@pytest.fixture(scope="function")
def user_template() -> list:
    return [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]


def test_when_first_name_not_exist(user_template: list) -> None:
    del user_template[0]["first_name"]
    restore_names(user_template)
    assert "first_name" in user_template[0]


def test_when_first_name_is_none(user_template: list) -> None:
    user_template[0]["first_name"] = None
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Jack"
