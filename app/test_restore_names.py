import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_users",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            id="restore first_name when value is none",
        ),
        pytest.param(
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            id="restore first_name when key is missing",
        ),
        pytest.param(
            [
                {
                    "first_name": "Robert",
                    "last_name": "Martin",
                    "full_name": "Bob Martin",
                }
            ],
            [
                {
                    "first_name": "Robert",
                    "last_name": "Martin",
                    "full_name": "Bob Martin",
                }
            ],
            id="keep existing first_name unchanged",
        ),
    ],
)
def test_restore_names_updates_users(
    users: list[dict],
    expected_users: list[dict],
) -> None:
    restore_names(users)

    assert users == expected_users


def test_restore_names_returns_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    assert restore_names(users) is None
