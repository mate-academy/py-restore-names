import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,result",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            [
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
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": "Hatfield",
                    "full_name": "James Hatfield",
                },
                {
                    "first_name": None,
                    "last_name": "Ulrich",
                    "full_name": "Lars Ulrich",
                },
            ],
            [
                {
                    "first_name": "James",
                    "last_name": "Hatfield",
                    "full_name": "James Hatfield",
                },
                {
                    "first_name": "Lars",
                    "last_name": "Ulrich",
                    "full_name": "Lars Ulrich",
                }
            ]
        )
    ]
)
def test_restore_names(users: list, result: list) -> None:
    restore_names(users)
    assert users == result
