import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list[dict]:
    return [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_restore_name_without_first_name(user_template: list[dict]) -> None:
    restore_names(user_template)
    assert user_template[0].get("first_name") == "Mike"


def test_restore_name_with_none_first_name(user_template: list[dict]) -> None:
    user_template[0]["first_name"] = None
    restore_names(user_template)
    assert user_template[0].get("first_name") == "Mike"
