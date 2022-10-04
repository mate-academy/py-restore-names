import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,restore_name",
    [
        (
            [
                {
                    "first_name": "Homer",
                    "last_name": "Simpson",
                    "full_name": "Homer Simpson",
                }
            ],
            [
                {
                    "first_name": "Homer",
                    "last_name": "Simpson",
                    "full_name": "Homer Simpson",
                }
            ],
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": "Simpson",
                    "full_name": "Bart Simpson",
                }
            ],
            [
                {
                    "first_name": "Bart",
                    "last_name": "Simpson",
                    "full_name": "Bart Simpson",
                }
            ],
        ),
        (
            [
                {
                    "last_name": "Simpson",
                    "full_name": "Homer Simpson",
                },
                {
                    "last_name": "Simpson",
                    "full_name": "Bart Simpson",
                }
            ],
            [
                {
                    "first_name": "Homer",
                    "last_name": "Simpson",
                    "full_name": "Homer Simpson",
                },
                {
                    "first_name": "Bart",
                    "last_name": "Simpson",
                    "full_name": "Bart Simpson",
                }
            ],
        ),
        ([], []),
    ]
)
def test_restore_name(users, restore_name):
    restore_names(users)
    assert users == restore_name, (
        "'restore_names' should restore 'first_name' value"
    )
