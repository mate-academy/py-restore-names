import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        ({"first_name": None, "last_name": "Doe", "full_name": "John Doe"},
         {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"}),
        ({"last_name": "Manko", "full_name": "Artem Manko"},
         {"first_name": "Artem", "last_name": "Manko", "full_name": "Artem Manko"}),
    ]
)
def test_restore_names(users, expected):
    restore_names([users])
    assert users == expected
