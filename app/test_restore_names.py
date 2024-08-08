import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, user_list",
    [
        (
            [
                {"first_name": None, "full_name": "Jack Holy"},
                {"full_name": "Mike Adams"}
            ],
            [
                {"first_name": "Jack", "full_name": "Jack Holy"},
                {"first_name": "Mike", "full_name": "Mike Adams"}
            ]
        ),
    ]
)
def test_restore_names(
        users: list,
        user_list: list
) -> None:
    restore_names(users)
    assert users == user_list
