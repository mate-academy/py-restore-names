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
        },
    ]


def test_restore_names(user_template: list) -> None:
    users = user_template
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
