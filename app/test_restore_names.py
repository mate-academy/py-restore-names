import pytest

from app.restore_names import restore_names


def test_restore_names_missing_first_name() -> None:
    users = [
        {"last_name": "Smith", "full_name": "John Smith"},
        {
            "first_name": None,
            "last_name": "Brown",
            "full_name": "Alice Brown",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Alice"


def test_restore_names_with_existing_first_name() -> None:
    users = [
        {
            "first_name": "Emma",
            "last_name": "White",
            "full_name": "Emma White",
        },
        {
            "first_name": "Liam",
            "last_name": "Johnson",
            "full_name": "Liam Johnson",
        },
    ]
    original = [user.copy() for user in users]
    restore_names(users)
    assert users == original


def test_restore_names_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


@pytest.mark.parametrize(
    "users, expected_first_names",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Hill",
                    "full_name": "Robert Hill",
                },
                {
                    "last_name": "Davis",
                    "full_name": "Lucy Davis",
                },
                {
                    "first_name": "Mark",
                    "last_name": "King",
                    "full_name": "Mark King",
                },
            ],
            ["Robert", "Lucy", "Mark"],
        ),
    ],
)
def test_restore_names_multiple_missing(
    users: list[dict],
    expected_first_names: list[str],
) -> None:
    restore_names(users)
    result = [user["first_name"] for user in users]
    assert result == expected_first_names
