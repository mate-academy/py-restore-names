import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("users_input", [
    {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
    {"last_name": "Holy", "full_name": "Jack Holy"},
    {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"}
]
)
def test_when_first_name_is_none(users_input: dict) -> None:
    users = [users_input]
    restore_names(users)
    assert users_input == {
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }
