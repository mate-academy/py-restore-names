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
      "full_name": "Mike Adams",
    },
     {
      "first_name": "David",
      "last_name": "Jason",
      "full_name": "David Jason",
    }]


def test_check_data_(users):
    # change users
    restore_names(users)
    assert users == [{"first_name": "Jack",
                      "last_name": "Holy",
                      "full_name": "Jack Holy",
                      },
                     {"first_name": "Mike",
                      "last_name": "Adams",
                      "full_name": "Mike Adams",
                      },
                     {"first_name": "David",
                      "last_name": "Jason",
                      "full_name": "David Jason",
                      }]
