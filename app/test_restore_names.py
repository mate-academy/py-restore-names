import pytest
from app.restore_names import restore_names


def run_restore_and_check(user: dict, expected: str) -> None:
    users = [user]
    restore_names(users)
    assert users[0]["first_name"] == expected


@pytest.mark.parametrize(
    "user, expected",
    [
        ({
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"}, "Jack"),
        ({
            "last_name": "Adams",
            "full_name": "Mike Adams"}, "Mike")
    ]
)
def test_restore_names(user: dict, expected: str) -> None:
    run_restore_and_check(user, expected)
