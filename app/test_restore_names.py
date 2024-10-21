import pytest
from app.restore_names import restore_names


@pytest.fixture(scope="function")
def users_data():
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


def test_restored_name(users_data):
    restore_names(users_data)
    assert users_data[0]["first_name"] == "Jack"
    assert users_data[1]["first_name"] == "Mike"
