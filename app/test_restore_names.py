import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        (
            [{
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }],
            [{
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }]
        ),
        (
            [{
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }],
            [{
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }]
        ),
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
            [{
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }],
            [{
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }]
        )
    ]
)
def test_restore_names(users: list[dict], expected: list[dict]) -> None:
    restore_names(users)

    assert users == expected


def test_restore_names_should_return_none() -> None:
    users = [{
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }]

    assert restore_names(users) is None
