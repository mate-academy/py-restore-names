import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_first_names",
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
                {
                    "first_name": "Anna",
                    "last_name": "Smith",
                    "full_name": "Anna Smith",
                },
            ],
            ["Jack", "Mike", "Anna"],
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "first_name": None,
                    "last_name": "Smith",
                    "full_name": "Anna Smith",
                },
            ],
            ["Jack", "Anna"],
        ),
        (
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
                {
                    "last_name": "Brown",
                    "full_name": "Lisa Brown",
                },
            ],
            ["Mike", "Lisa"],
        ),
        (
            [
                {
                    "first_name": "Sam",
                    "last_name": "Green",
                    "full_name": "Sam Green",
                },
                {
                    "first_name": "Liz",
                    "last_name": "Blue",
                    "full_name": "Liz Blue",
                },
            ],
            ["Sam", "Liz"],
        ),
    ],
)
def test_restore_names(
    users: list[dict[str, str | None]], expected_first_names: list[str]
) -> None:
    restore_names(users)
    for user, expected_name in zip(users, expected_first_names):
        assert user["first_name"] == expected_name
