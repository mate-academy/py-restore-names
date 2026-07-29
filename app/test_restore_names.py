import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "given_users,expected_users",
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
    ]
)
def test_should_add_first_name(
        given_users: list[dict],
        expected_users: list[dict]
) -> None:
    restore_names(given_users)
    assert given_users == expected_users
