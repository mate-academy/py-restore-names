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
                    "surname": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            ["Jack", "Mike"],
        ),
        (
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                },
            ],
            ["Jack", "Mike"],
        ),
    ],
)
def test_restore_names_two_users(
        users: list,
        expected_first_names: list
) -> None:
    restore_names(users)

    assert [user["first_name"] for user in users] == expected_first_names
