import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ],
        ),
        (
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                }
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                }
            ],
        ),
        (
            [
                {
                    "first_name": "Johnny",
                    "last_name": "Smith",
                    "full_name": "John Smith"
                }
            ],
            [
                {
                    "first_name": "Johnny",
                    "last_name": "Smith",
                    "full_name": "John Smith"
                }
            ],
        ),
        (
            [],
            [],
        ),
    ],
    ids=[
        "first_name is None",
        "first_name is missing",
        "existing first_name is not changed",
        "empty list",
    ],
)
def test_restore_names(users: list, expected: list) -> None:
    restore_names(users)
    assert users == expected


def test_restore_names_with_mixed_users() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "Ann", "last_name": "Lee", "full_name": "Ann Lee"},
    ]
    restore_names(users)
    assert [user["first_name"] for user in users] == ["Jack", "Mike", "Ann"]


def test_restore_names_should_return_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]
    assert restore_names(users) is None
