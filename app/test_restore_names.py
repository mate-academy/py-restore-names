import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "list_users, result",
    [
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
        )
    ],
    ids=[
        "Restore first_name from full_name if missing or None"
    ])
def test_restore_names(list_users: list, result: list) -> None:
    restore_names(list_users)
    assert list_users == result
