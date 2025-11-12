import pytest

from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list[dict]:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_restore_names_with_none(user_template: list) -> None:
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Jack"


def test_restore_names_without_first_name(user_template: list) -> None:
    del user_template[0]["first_name"]
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Jack"


def test_restore_name_first_name_already_filled(user_template: list) -> None:
    user_template[0]["first_name"] = "Jack"
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Jack"
