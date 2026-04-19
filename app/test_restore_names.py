import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "initial_user, expected_first_name",
    [
        ({"last_name": "Adams",
          "full_name": "Mike Adams"}, "Mike"),
        ({"first_name": None,
          "last_name": "Holy", "full_name": "Jack Holy"}, "Jack"),
    ],
)
def test_restore_names_works_with_missing_or_none_values(
    initial_user: dict,
    expected_first_name: str
) -> None:
    users = [initial_user]
    restore_names(users)
    assert users[0]["first_name"] == expected_first_name


def test_restore_names_does_not_overwrite_existing_data() -> None:
    users = [
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "full_name": "Alice Smith",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Alice"


def test_restore_names_handles_multiple_users_at_once() -> None:
    users = [
        {"full_name": "John Doe", "last_name": "Doe"},
        {"first_name": None, "full_name": "Jane Doe", "last_name": "Doe"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Jane"
