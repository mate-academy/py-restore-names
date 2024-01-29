import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list:
    return [{
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }]


def test_should_set_up_first_name_if_user_has_no_first_name(
        user_template: list
) -> None:
    del user_template[0]["first_name"]
    user = user_template
    restore_names(user)
    assert "first_name" in user[0].keys()


def test_should_set_up_first_name_if_user_first_name_is_none(
        user_template: list
) -> None:
    user_template[0]["first_name"] = None
    user = user_template
    restore_names(user)
    assert user[0]["first_name"] == "Jack"
