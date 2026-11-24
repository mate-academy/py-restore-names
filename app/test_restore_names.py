import pytest


from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list[dict]:
    return [{
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }]


def test_should_restore_when_name_is_none(user_template: list[dict]) -> None:
    user_template[0]["first_name"] = None
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Jack"


def test_should_restore_when_name_is_delete(user_template: list[dict]) -> None:
    del user_template[0]["first_name"]
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Jack"


def test_should_do_nothin_when_we_have_name(user_template: list[dict]) -> None:
    assert restore_names(user_template) is None
