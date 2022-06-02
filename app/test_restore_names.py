import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user_without_first_name, user_with_first_name",
    [
        pytest.param(
            [{"first_name": None,
              "last_name": "Holy",
              "full_name": "Jack Holy"}],
            [{"first_name": "Jack",
              "last_name": "Holy",
              "full_name": "Jack Holy"}],
        ),
        pytest.param(
            [{"last_name": "Adams",
              "full_name": "Mike Adams"}],
            [{"first_name": "Mike",
              "last_name": "Adams",
              "full_name": "Mike Adams"}],
        )
    ]
)
def test_restore_name(user_without_first_name, user_with_first_name):
    users = user_without_first_name
    restore_names(users)
    assert users == user_with_first_name
