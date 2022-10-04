import pytest
from app.restore_names import restore_names


@pytest.fixture
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


def test_restore_names(user_template):
    users = user_template
    result = [
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

    restore_names(users)

    assert users == result


def test_restore_names_should_return_none(user_template):
    assert restore_names(user_template) is None
