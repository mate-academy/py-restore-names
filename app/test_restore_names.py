import pytest
from app.restore_names import restore_names


@pytest.fixture
def users_data() -> list:
    return [
        {"first_name": None, "last_name": "Smith", "full_name": "Alice Smith"},
        {"last_name": "Jones", "full_name": "Bob Jones"},
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
    ]


def test_restore_names_with_fixture(users_data: list) -> None:
    restore_names(users_data)
    expected_output = [
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "full_name": "Alice Smith"
        },
        {"first_name": "Bob", "last_name": "Jones", "full_name": "Bob Jones"},
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
    ]
    assert users_data == expected_output
