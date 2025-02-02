import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        ([{"full_name": "John Doe", "first_name": None}],
         [{"full_name": "John Doe", "first_name": "John"}]),
        ([{"full_name": "Bob Johnson"}],
         [{"full_name": "Bob Johnson", "first_name": "Bob"}]),
        ([{"full_name": "Alice Johnson"}],
         [{"full_name": "Alice Johnson", "first_name": "Alice"}]),
    ],
)
def test_restore_names(users: dict, expected: dict) -> None:
    restore_names(users)
    assert users == expected
