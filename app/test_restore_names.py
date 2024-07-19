import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users",
    [
        [
            {"full_name": "John Doe", "first_name": None, "last_name": "Doe"},
            {"full_name": "Jane Doe", "first_name": "Jane", "last_name": "Doe"},
            {"full_name": "Jack Doe",  "last_name": "Doe"},
        ]
    ],
)
def test_restore_names(users):
    restore_names(users)
    assert users == [
        {"full_name": "John Doe", "first_name": "John", "last_name": "Doe"},
        {"full_name": "Jane Doe", "first_name": "Jane", "last_name": "Doe"},
        {"full_name": "Jack Doe", "first_name": "Jack", "last_name": "Doe"},
    ]