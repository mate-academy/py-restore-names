import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_temp():
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


def test_first_name_is_missing_or_equal_none(users_temp):
    restore_names(users_temp)
    assert users_temp == [
      {
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy",
      },
      {
        "first_name": "Mike",
        "last_name": "Adams",
        "full_name": "Mike Adams",
      },
    ]
