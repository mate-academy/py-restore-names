import pytest
from app.restore_names import restore_names

@pytest.mark.parametrize(
    "users, expected",
    [
        (
            [
                {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
            ],
            [
                {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
            ],
        ),
        (
            [
                {"last_name": "Adams", "full_name": "John Adams"},
            ],
            [
                {"first_name": "John", "last_name": "Adams", "full_name": "John Adams"},
            ],
        ),
    ],
)
def test_full_name(users: list, expected: list) -> None:
    restore_names(users)
    assert users == expected
