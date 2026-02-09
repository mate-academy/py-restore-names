import pytest
import copy
from app import restore_names


@pytest.mark.parametrize(
    "users,expected",
    [
        (
            [{"first_name": None,
              "last_name": "Holy",
              "full_name": "Jack Holy"}],
            [{"first_name": "Jack",
              "last_name": "Holy",
              "full_name": "Jack Holy"}],
        ),
        (
            [{"last_name": "Adams",
              "full_name": "Mike Adams"}],
            [{"first_name": "Mike",
              "last_name": "Adams",
              "full_name": "Mike Adams"}],
        ),
        (
            [{"first_name": "Bob",
              "last_name": "Black",
              "full_name": "Bob Black"}],
            [{"first_name": "Bob",
              "last_name": "Black", "full_name": "Bob Black"}],
        ),
        (
            [{"first_name": None,
              "full_name": "Jane"}],
            [{"first_name": "Jane",
              "full_name": "Jane"}],
        )
    ]
)
def test_restore_names(
        users: list[dict],
        expected: list[dict]
) -> None:
    users_copy = copy.deepcopy(users)
    restore_names.restore_names(users_copy)
    assert users_copy == expected
