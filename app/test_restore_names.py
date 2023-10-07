import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users():
    return users == [
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


def test_restore_names(users) -> None:
    for user in users:
        if "first_name" not in user or user["first_name"] is None:
            assert user["first_name"] == user["full_name"].split()[0]
