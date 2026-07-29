import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("users, expected", [
    ([
        {"full_name": "John Doe"},
        {"full_name": "Alice Smith", "first_name": None},
    ], [
        {"full_name": "John Doe", "first_name": "John"},
        {"full_name": "Alice Smith", "first_name": "Alice"},
    ]),
    ([
        {"full_name": "Bob Johnson", "first_name": "Bob"},
        {"full_name": "Eve Anderson", "first_name": "Eve"},
    ], [
        {"full_name": "Bob Johnson", "first_name": "Bob"},
        {"full_name": "Eve Anderson", "first_name": "Eve"},
    ]),
    ([
        {"full_name": "Grace Brown"},
        {"full_name": "Daniel Lee", "first_name": "Daniel"},
        {"full_name": "Sophia Taylor", "first_name": None},
    ], [
        {"full_name": "Grace Brown", "first_name": "Grace"},
        {"full_name": "Daniel Lee", "first_name": "Daniel"},
        {"full_name": "Sophia Taylor", "first_name": "Sophia"},
    ]),
])
def test_restore_names(
        users: list,
        expected: str
) -> None:
    restore_names(users)
    assert users == expected
