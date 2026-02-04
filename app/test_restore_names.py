import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_first_name",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            "Jack",
        ),
        (
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            "Mike",
        ),
    ],
)
def test_restore_first_name(
    users: list[dict],
    expected_first_name: str,
) -> None:
    restore_names(users)

    assert users[0]["first_name"] == expected_first_name


def test_does_not_override_existing_first_name() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "Jack Doe",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"


def test_restore_names_for_multiple_users() -> None:
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
