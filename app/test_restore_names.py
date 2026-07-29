import pytest
from app import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        # first_name is None — must be restored
        [[{"first_name": None, "last_name": "Holy",
           "full_name": "Jack Holy"}],
         [{"first_name": "Jack", "last_name": "Holy",
           "full_name": "Jack Holy"}]],

        ([{"first_name": None, "last_name": "Holy",
           "full_name": "Din Holy"}],
         [{"first_name": "Din", "last_name": "Holy",
           "full_name": "Din Holy"}]),

        # first_name key is missing entirely — must be restored
        ([{"last_name": "Adams", "full_name": "Mike Adams"}],
         [{"first_name": "Mike", "last_name": "Adams",
           "full_name": "Mike Adams"}]),

        # first_name already present — must NOT be changed
        ([{"first_name": "Alice", "last_name": "Swift",
           "full_name": "Alice Swift"}],
         [{"first_name": "Alice", "last_name": "Swift",
           "full_name": "Alice Swift"}]),

        # Mixed list
        ([{"first_name": None, "full_name": "John Doe"},
          {"full_name": "Jane Doe"}],
         [{"first_name": "John", "full_name": "John Doe"},
          {"first_name": "Jane", "full_name": "Jane Doe"}]),
    ]
)
def test_restore_names(users: None, expected: None) -> None:
    restore_names.restore_names(users)
    assert users == expected


def test_first_name_is_none_is_restored() -> None:
    users = [{"first_name": None, "full_name": "Jack Holy"}]
    restore_names.restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_missing_first_name_key_is_restored() -> None:
    users = [{"full_name": "Mike Adams"}]
    restore_names.restore_names(users)
    assert users[0]["first_name"] == "Mike"
