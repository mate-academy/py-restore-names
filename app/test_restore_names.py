import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize("user, expected_first_name", [
    ({"full_name": "John Doe"}, "John"),
    ({"full_name": "John Doe", "first_name": "Jane"}, "Jane"),
    ({"full_name": "Alice Smith", "first_name": None}, "Alice"),
    ({"full_name": "Michael Brown", "first_name": "Michael"}, "Michael")
])
def test_restore_names(user: dict, expected_first_name: str) -> None:
    # Act
    restore_names([user])

    # Assert
    assert user["first_name"] == expected_first_name


def test_restore_names_no_users() -> None:
    # Arrange
    users = []

    # Act
    restore_names(users)

    # Assert
    assert len(users) == 0
