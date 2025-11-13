import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "initial_users, expected_users",
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
                    "first_name": "Sarah",
                    "last_name": "Connor",
                    "full_name": "Sarah Connor",
                },
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "John Doe",
                },
            ],
            [
                {
                    "first_name": "Sarah",
                    "last_name": "Connor",
                    "full_name": "Sarah Connor",
                },
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "John Doe",
                },
            ],
        ),

        (
            [
                {
                    "first_name": "Valid",
                    "last_name": "Name",
                    "full_name": "Valid Name",
                },
                {
                    "first_name": None,
                    "last_name": "Baggins",
                    "full_name": "Bilbo Baggins",
                },
            ],
            [
                {
                    "first_name": "Valid",
                    "last_name": "Name",
                    "full_name": "Valid Name",
                },
                {
                    "first_name": "Bilbo",
                    "last_name": "Baggins",
                    "full_name": "Bilbo Baggins",
                },
            ],
        ),

        (
            [],
            [],
        ),
    ],
)
def test_restore_names_modifies_list_in_place(
    initial_users: list,
    expected_users: list
) -> None:

    restore_names(initial_users)
    assert initial_users == expected_users
