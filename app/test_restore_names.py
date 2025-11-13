import pytest
from app.restore_names import restore_names
from typing import List


@pytest.mark.parametrize(
    "initial_users, expected_users",
    [
        (
            [{"last_name": "Holy", "full_name": "Jack Holy"}],
            [{"first_name": "Jack", "last_name":
                "Holy", "full_name": "Jack Holy"}],
        ),
        (
            [{"first_name": None, "last_name": "Adams",
              "full_name": "Mike Adams"}],
            [{"first_name": "Mike", "last_name": "Adams",
              "full_name": "Mike Adams"}],
        ),
        (
            [{"first_name": "Original", "last_name": "User",
              "full_name": "Jack Holy"}],
            [{"first_name": "Original", "last_name": "User",
              "full_name": "Jack Holy"}],
        ),
        (
            [
                {"first_name": None, "last_name": "Smith",
                 "full_name": "Tim Smith"},
                {"first_name": "Max", "last_name": "Hardy",
                 "full_name": "Max Hardy"},
                {"last_name": "Brown", "full_name": "Charlie Brown"},
            ],
            [
                {"first_name": "Tim", "last_name": "Smith",
                 "full_name": "Tim Smith"},
                {"first_name": "Max", "last_name": "Hardy",
                 "full_name": "Max Hardy"},
                {"first_name": "Charlie", "last_name": "Brown",
                 "full_name": "Charlie Brown"},
            ],
        ),
        ([], []),
        (
            [{"first_name": "", "last_name": "Empty",
              "full_name": "Empty Name"}],
            [{"first_name": "", "last_name": "Empty",
              "full_name": "Empty Name"}],
        ),
    ],
    ids=[
        "Missing first name",
        "First name is None",
        "First name is present name",
        "Mixed list of first names",
        "Empty list",
        "Empty string in present name"
    ]
)
def test_restore_names(
        initial_users: List[dict],
        expected_users: List[dict]
) -> None:
    restore_names(initial_users)

    assert initial_users == expected_users
