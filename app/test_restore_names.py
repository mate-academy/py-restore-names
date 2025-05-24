import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("users, expected", [
    (
        [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "first_name": None,
                "last_name": "Adams",
                "full_name": "Mike Adams"
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
                "full_name": "Mike Adams"
            },
        ],
    ),
    (
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
        ],
    ),
    (
        [
            {
                "first_name": None,
                "full_name": "Alice Johnson",
            },
            {
                "first_name": "Alice",
                "full_name": "Alice Johnson"
            }
        ],
        [
            {
                "first_name": "Alice",
                "full_name": "Alice Johnson",
            },
            {
                "first_name": "Alice",
                "full_name": "Alice Johnson"
            }
        ],
    ),
    (
        [
            {
                "first_name": "Emma",
                "last_name": "Brown",
                "full_name": "Emma Brown",
            },
            {
                "first_name": "Emma",
                "last_name": "Brown",
                "full_name": "Emma Brown"
            }
        ],
        [
            {
                "first_name": "Emma",
                "last_name": "Brown",
                "full_name": "Emma Brown",
            },
            {
                "first_name": "Emma",
                "last_name": "Brown",
                "full_name": "Emma Brown"
            }
        ],
    ),
    (
        [],
        [],
    ),
])
def test_restore_names(users: list, expected: list) -> None:
    restore_names(users)
    assert users == expected


def test_restore_names_does_not_return() -> None:
    users = [{"first_name": None, "full_name": "Alice Johnson"}]
    result = restore_names(users)
    assert result is None
