import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "damaged_users, restored_users",
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
            ],
        ),
        (
            [
                {
                    "last_name": "Pavliuk",
                    "full_name": "Petro Pavliuk",
                },
                {
                    "last_name": "Petrenko",
                    "full_name": "Ivan Petrenko",
                },
            ],
            [
                {
                    "first_name": "Petro",
                    "last_name": "Pavliuk",
                    "full_name": "Petro Pavliuk",
                },
                {
                    "first_name": "Ivan",
                    "last_name": "Petrenko",
                    "full_name": "Ivan Petrenko",
                },
            ],
        )
    ],
)
def test_restore_names_works_correctly(damaged_users, restored_users) -> None:
    restore_names(damaged_users)
    assert damaged_users == restored_users
