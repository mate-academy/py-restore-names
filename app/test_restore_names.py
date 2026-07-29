import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "list_users, expected",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Smith",
                    "full_name": "John Smith",
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Smith",
                    "full_name": "John Smith",
                },
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ]
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
                    "full_name": "Mike Adams",
                }
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
                }
            ]
        )
    ],
    ids=[
        "first_name: None and not in, expected: first_name, add first_name",
        "first_name: already, expected: Do nothing",
    ]
)
def test_restore_names(list_users: list[dict], expected: list[dict]) -> None:
    restore_names(list_users)
    assert list_users == expected
