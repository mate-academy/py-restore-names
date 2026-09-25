import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ],
        ),
        (
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
        ),
        (
            [
                {
                    "first_name": "Anna",
                    "last_name": "Smith",
                    "full_name": "Anna Smith",
                },
            ],
            [
                {
                    "first_name": "Anna",
                    "last_name": "Smith",
                    "full_name": "Anna Smith",
                },
            ],
        ),
    ],
    ids=[
        "first_name is None",
        "first_name is missing",
        "first_name is already set",
    ],
)
def test_restore_names(users: list, expected: list) -> None:
    assert restore_names(users) is None
    assert users == expected


def test_restore_names_mixed_users() -> None:
    users = [
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
    restore_names(users)
    assert users == [
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
