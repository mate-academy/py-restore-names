import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_restore_names(user_template: list) -> None:
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Jack"
    assert user_template[1]["first_name"] == "Mike"
