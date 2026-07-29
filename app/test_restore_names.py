import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, users_result",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ]
        ),
        (
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                }
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                }
            ]
        )
    ],
    ids=[
        "first name is None",
        "no first name"
    ]
)
def test_restore_names(
        users: list,
        users_result: list
) -> None:
    restore_names(users)
    assert users == users_result
