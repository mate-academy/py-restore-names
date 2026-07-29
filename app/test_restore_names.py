import pytest
from app.restore_names import restore_names


@pytest.fixture()
def template_user() -> list:
    users = [
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

    return users


def test_restore_users(template_user: list) -> None:
    restore_names(template_user)
    for user in template_user:
        assert "first_name" in user and user["first_name"] is not None
