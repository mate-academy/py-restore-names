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
                {
                    "first_name": None,
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                }
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
                }
            ]
        ),
        (
            [
                {
                    "last_name": "Doe",
                    "full_name": "John Doe"
                },
                {
                    "last_name": "Smith",
                    "full_name": "Jane Smith"
                }
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "John Doe"
                },
                {
                    "first_name": "Jane",
                    "last_name": "Smith",
                    "full_name": "Jane Smith"
                }
            ]
        ),
        (
            [
                {
                    "first_name": "Alice",
                    "last_name": "Cooper",
                    "full_name": "Alice Cooper"
                },
                {
                    "first_name": "Bob",
                    "last_name": "Marley",
                    "full_name": "Bob Marley"
                }
            ],
            [
                {
                    "first_name": "Alice",
                    "last_name": "Cooper",
                    "full_name": "Alice Cooper"
                },
                {
                    "first_name": "Bob",
                    "last_name": "Marley",
                    "full_name": "Bob Marley"
                }
            ]
        )
    ],
    ids=[
        "first_name_is_none",
        "first_name_is_missing",
        "first_name_is_present"
    ]
)
def test_restore_names(users: list[dict], expected: list[dict]) -> None:
    """
    Test restore_names to ensure first_name is restored correctly.
    """
    restore_names(users)
    assert users == expected, f"Expected {expected}, but get {users}"
