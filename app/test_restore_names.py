import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("users, expected_first_names", [
    (
        [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy"
            }
        ],
        ["Jack"]
    ),
    (
        [
            {
                "last_name": "Adams",
                "full_name": "Michael Adams"
            }
        ],
        ["Michael"]
    ),
    (
        [
            {
                "first_name": "Anna",
                "last_name": "Simpson",
                "full_name": "Anna Simpson"
            }
        ],
        ["Anna"]
    ),
    (
        [
            {
                "first_name": None,
                "last_name": "Brown",
                "full_name": "Cleveland Brown"
            },
            {
                "last_name": "Black",
                "full_name": "Luk Black"
            },
            {
                "first_name": "Mark",
                "last_name": "Antonie",
                "full_name": "Mark Antonie"
            },
        ],
        ["Cleveland", "Luk", "Mark"]
    )
])
def test_restore_names(users: list[dict], expected_first_names: str) -> None:
    restore_names(users)

    for user, expected_first_name in zip(users, expected_first_names):
        assert user["first_name"] == expected_first_name
