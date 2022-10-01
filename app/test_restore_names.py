import pytest

from app.restore_names import restore_names


@pytest.fixture()
def user_template():
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


def test_first_name_verification(user_template):
    restore_names(user_template)
    for user in user_template:
        assert "first_name" in user, "The user must have a first name"
        assert type(user["first_name"]) == str, \
            "A user's first name must be a string"
