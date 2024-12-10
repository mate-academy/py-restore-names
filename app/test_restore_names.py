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
                },
                {"last_name": "Adams", "full_name": "Mike Adams"},
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                },
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                },
            ],
        ),
        (
            [
                {
                    "first_name": "Emily",
                    "last_name": "Smith",
                    "full_name": "Emily Smith"
                },
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "John Doe"
                },
            ],
            [
                {
                    "first_name": "Emily",
                    "last_name": "Smith",
                    "full_name": "Emily Smith"
                },
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "John Doe"
                },
            ],
        ),
        ([], []),
        (
            [{
                "first_name": None,
                "last_name": "Brown",
                "full_name": "Laura Brown"
            }],
            [{
                "first_name": "Laura",
                "last_name": "Brown",
                "full_name": "Laura Brown"
            }],
        ),
    ],
)
def test_restore_names(users: list, expected: list) -> None:
    restore_names(users)
    assert users == expected
