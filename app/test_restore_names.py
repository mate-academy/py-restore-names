import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_users,expected_users",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                },
                {
                    "first_name": "Anna",
                    "last_name": "Smith",
                    "full_name": "Anna Smith"
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                },
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                },
                {
                    "first_name": "Anna",
                    "last_name": "Smith",
                    "full_name": "Anna Smith"
                }
            ]
        )
    ]
)
def test_correct_restore_names(
        input_users: list[dict],
        expected_users: list[dict]
) -> None:
    restore_names(input_users)
    assert input_users == expected_users
