import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user, expected_first_name",
    [
        (
            {"first_name": None, "full_name": "Jack Holy"},
            "Jack",
        ),
        (
            {"last_name": "Adams", "full_name": "Mike Adams"},
            "Mike",
        ),
        (
            {"first_name": "Alise", "full_name": "Alise Cooper"},
            "Alise",
        ),
        (
            {"first_name": None, "full_name": "   Sarah   Connor  "},
            "Sarah",
        ),
    ],
)
def test_restore_names_parametrized(
        user: dict,
        expected_first_name: str
) -> None:
    users = [user]

    restore_names(users)

    assert users[0]["first_name"] == expected_first_name
