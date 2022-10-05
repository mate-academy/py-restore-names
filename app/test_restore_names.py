import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list[dict]:
    return [
        {
            "first_name": None,
            "last_name": "Holly",
            "full_name": "Jack Holly",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_restore_first_names(user_template: list[dict]) -> None:
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Jack"
    assert user_template[1]["first_name"] == "Mike"


def test_restore_first_name_neo(user_template: list[dict]) -> None:
    user_template[0]["full_name"] = "Keanu Reeves"
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Keanu"
