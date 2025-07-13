import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_users",
    [
        (
            [{"first_name": None, "full_name": "Jack Holy"}],
            [{"first_name": "Jack", "full_name": "Jack Holy"}]
        ),
        (
            [{"full_name": "Mike Adams"}],
            [{"first_name": "Mike", "full_name": "Mike Adams"}]
        ),
        ([], [])
    ],
    ids=[
        "first name is None",
        "first name is absent in the dict",
        "empty lists"
    ]
)
def test_restore_names(users: list, expected_users: list) -> None:
    restore_names(users)
    assert users == expected_users
