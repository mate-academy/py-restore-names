import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,added_first_name",
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
                {
                    "first_name": "Paul",
                    "last_name": "Andersson",
                    "full_name": "Paul Andersson",
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
                {
                    "first_name": "Paul",
                    "last_name": "Andersson",
                    "full_name": "Paul Andersson",
                },
            ],
        ),
    ],
)
def test_restore_names(users: list, added_first_name: list) -> None:
    restore_names(users)
    assert users == added_first_name, (
        f"The list {users} mas to be equal " f"to the list {added_first_name}"
    )
