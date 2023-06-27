from app.restore_names import restore_names
import pytest


@pytest.fixture()
def user_template() -> list[dict]:
    return [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]


def test_first_name_is_none(user_template: list[dict]) -> None:
    user_template[0]["first_name"] = None
    user_template[1]["first_name"] = None
    restore_names(user_template)

    assert user_template[0].get("first_name") == "Jack"
    assert user_template[1].get("first_name") == "Mike"


def test_first_name_does_not_exist(user_template: list[dict]) -> None:
    restore_names(user_template)

    assert user_template[0].get("first_name") == "Jack"
    assert user_template[1].get("first_name") == "Mike"
