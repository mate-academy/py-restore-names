import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,users_with_restored_names",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
        ),
        (
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
        ),
        ([], []),
    ],
)
def test_restore_names(users, users_with_restored_names):
    restore_names(users)
    assert users == users_with_restored_names, (
        "Function 'restore_names' should restore 'first_name' value "
        "for users in the given list"
    )
