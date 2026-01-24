import pytest
from typing import Any

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        (
            [
                {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
                {"last_name": "Adams", "full_name": "Mike Adams"},
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
            ],
        ),
        (
            [
                {
                    "first_name": "Anna",
                    "last_name": "Smith",
                    "full_name": "Anna Smith",
                },
                {
                    "first_name": None,
                    "last_name": "Jones",
                    "full_name": "Tom Jones",
                },
            ],
            [
                {
                    "first_name": "Anna",
                    "last_name": "Smith",
                    "full_name": "Anna Smith",
                },
                {
                    "first_name": "Tom",
                    "last_name": "Jones",
                    "full_name": "Tom Jones",
                },
            ],
        ),
        ([], []),
    ],
)
def test_restore_names_scenarios(
    users: list[dict[str, Any]],
    expected: list[dict[str, Any]],
) -> None:
    restore_names(users)

    assert users == expected
