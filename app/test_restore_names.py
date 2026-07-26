import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user, expected_first_name",
    [
        ({"last_name": "Jakob", "full_name": "Alex Jakob"}, "Alex"),
        ({"first_name": None, "full_name": "Alex Jakob"}, "Alex"),
        ({"first_name": "Sasha", "full_name": "Alex Jakob"}, "Sasha")
    ]
)
def test_first_name(user: dict, expected_first_name: str) -> None:
    restore_names([user])
    assert user["first_name"] == expected_first_name


def test_for_many_names() -> None:
    users = [
        {"first_name": "Sasha", "full_name": "Alex Jakob"},
        {"first_name": "Michel", "full_name": "Michel Black"},
        {"first_name": None, "full_name": "Walter White"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Sasha"
    assert users[1]["first_name"] == "Michel"
    assert users[2]["first_name"] == "Walter"
