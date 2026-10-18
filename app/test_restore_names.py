import pytest

from app.restore_names import restore_names


def test_restore_names_when_first_name_is_none_or_missing() -> None:
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

    result = restore_names(users)

    assert result is None
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


def test_restore_names_should_not_overwrite_existing_first_name() -> None:
    users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"


@pytest.mark.parametrize(
    "users_input,expected_users",
    [
        (
            [],
            [],
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": "Smith",
                    "full_name": "John Smith",
                }
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Smith",
                    "full_name": "John Smith",
                }
            ],
        ),
    ],
)
def test_restore_names_boundary_conditions(
    users_input: list[dict],
    expected_users: list[dict],
) -> None:
    restore_names(users_input)
    assert users_input == expected_users
