import pytest
from app.restore_names import restore_names


# fixture
@pytest.fixture()
def users_template():
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


def test_restore_names(users_template):
    restore_names(users_template)
    assert users_template[0]["first_name"] == "Jack"
    assert users_template[1]["first_name"] == "Mike"
    assert users_template[1]["full_name"] == "Mike Adams"
