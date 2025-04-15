import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_first_names",
    [
        (
            [{"first_name": None, "full_name": "Jack Holy"}],
            ["Jack"]
        ),
        (
            [{"first_name": "Anna", "full_name": "Anna Bell"}],
            ["Anna"]
        ),
        (
            [{"first_name": "Mike", "full_name": "Mike Adams"}],
            ["Mike"]
        ),
    ]
)
def test_restore_names(users: list, expected_first_names: list) -> None:
    restore_names(users)
    for user, expected in zip(users, expected_first_names):
        assert user["first_name"] == expected
