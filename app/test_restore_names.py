import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        (
            [
                {
                    "last_name": "Holy",
                    "full_name": "Moly Holy",
                },
                {
                    "first_name": None,
                    "last_name": "Bond",
                    "full_name": "James Bond",
                },
            ],
            [
                {
                    "first_name": "Moly",
                    "last_name": "Holy",
                    "full_name": "Moly Holy",
                },
                {
                    "first_name": "James",
                    "last_name": "Bond",
                    "full_name": "James Bond",
                }
            ]
        )
    ]
)
def test_restore(users: list, expected: list) -> None:
    restore_names(users)
    assert users == expected
