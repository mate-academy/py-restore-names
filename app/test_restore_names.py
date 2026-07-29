import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users",
    [
        ([{"first_name": "John",
           "last_name": "Doe",
           "full_name": "John Doe"}]),
        ([{"first_name": None,
           "last_name": "Jackson",
           "full_name": "Bob Jackson"}]),
        ([{"last_name": "Williams",
           "full_name": "Kevin Williams"}])
    ]
)
def test_restore_names(users: list) -> None:
    restore_names(users)
    for user in users:
        assert user["first_name"] == user["full_name"].split()[0]
