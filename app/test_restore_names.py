import pytest
from app.restore_names import restore_names


def test_restore_names(users: list) -> None:
    for user in users:
        if "first_name" not in user or user["first_name"] is None:
            user["first_name"] = user["full_name"].split()[0]


@pytest.mark.parametrize(
    "users, expected",
    [
        ([
             {"last_name": "Holy", "full_name": "Jack Holy"},
             {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"}
         ], [
             {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
             {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"}
         ]),
        ([
             {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
             {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"}
         ], [
             {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
             {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"}
         ]),
        ([
             {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
             {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"}
         ], [
             {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
             {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"}
         ]),
        ([], []),
        ([
             {"first_name": None, "last_name": "Holy"},
             {"last_name": "Adams"}
         ], [
             {"first_name": None, "last_name": "Holy"},
             {"last_name": "AdAMS"}
         ])
    ]
)
def test_restore_names(users, expected):
    restore_names(users)
    assert users == expected
