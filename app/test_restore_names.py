import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users():
    return [{
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy",
    },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"}]


def test_should_make_first_name_in_user(users):
    restore_names(users)
    for user in users:
        assert user["first_name"] == user["full_name"].split()[0]
