import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        (
            [{"last_name": "Doe",
              "full_name": "John Doe"}],
            [{"first_name": "John",
              "last_name": "Doe",
              "full_name": "John Doe"}]
        ),
        (
            [{"first_name": None,
              "last_name": "Doe",
              "full_name": "John Doe"}],
            [{"first_name": "John",
              "last_name": "Doe",
              "full_name": "John Doe"}]
        ),
        (
            [{"first_name": "John",
              "last_name": "Doe",
              "full_name": "John Doe"}],
            [{"first_name": "John",
              "last_name": "Doe",
              "full_name": "John Doe"}]
        ),
        (
            [{"last_name": "Smith",
              "full_name": "Jane Smith"},
             {"first_name": None,
              "last_name": "Jones",
              "full_name": "Bob Jones"},
             {"first_name": "Rick",
              "last_name": "Dalton",
              "full_name": "Rick Dalton"}],
            [{"first_name": "Jane",
              "last_name": "Smith",
              "full_name": "Jane Smith"},
             {"first_name": "Bob",
              "last_name": "Jones",
              "full_name": "Bob Jones"},
             {"first_name": "Rick",
              "last_name": "Dalton",
              "full_name": "Rick Dalton"}]
        )
    ],
    ids=[
        "Missing first name",
        "First name = None",
        "First name is already present",
        "Mixed cases"
    ]
)
def test_restore_names(users: list, expected: list) -> None:
    restore_names(users)
    assert users == expected
