import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_users, expected_first_names",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ],
            ["Jack"],
        ),
        (
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                }
            ],
            ["Mike"],
        ),
        (
            [
                {
                    "first_name": "Sam",
                    "last_name": "Smith",
                    "full_name": "Sam Smith"
                }
            ],
            ["Sam"],
        ),
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
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "full_name": "Jane Doe"
                }
            ],
            ["Jack", "Mike", "Jane"],
        ),
    ]
)
def test_should_restore_names(
        input_users: list[dict], expected_first_names: list[str]
) -> None:
    restore_names(input_users)
    assert [user["first_name"] for user in input_users] == expected_first_names
