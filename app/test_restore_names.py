import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_template():
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Brown",
            "full_name": "Anna Brown",
        },
    ]


def test_restore_first_name_none_and_empty(users_template):
    restore_names(users_template)
    assert users_template[0]["first_name"] == "Jack"
    assert users_template[1]["first_name"] == "Anna"
