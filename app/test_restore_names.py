from app.restore_names import restore_names
import pytest


@pytest.fixture()
def user():
    return user_data(
        [{"first_name": "Adam",
          "last_name": "Holy",
          "full_name": "Adam Holy",
          }]
    )


def test_if_first_name_none(user_data):
    user_data["first_name"] = None

    assert restore_names(user_data) == [
        {"first_name": "Adam",
         "last_name": "Holy",
         "full_name": "Adam Holy",
         }
    ]


def test_if_first_name_no_user_data(user_data):
    del user_data["first_name"]

    assert restore_names(user_data) == [
        {"first_name": "Adam",
         "last_name": "Holy",
         "full_name": "Adam Holy",
         }
    ]


def test_if_first_name_norm_user_data(user_data):

    assert restore_names(user_data) == [
        {"first_name": "Adam",
         "last_name": "Holy",
         "full_name": "Adam Holy",
         }
    ]
