import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user, expected_first_name",
    [
        ({"full_name": "Jack Holy"}, "Jack"),
        ({"full_name": "Jack Holy", "first_name": None}, "Jack"),
    ],
)
def test_restore_first_name(user: dict, expected_first_name: str) -> None:
    users = [user]

    restore_names(users)

    assert users[0]["first_name"] == expected_first_name
