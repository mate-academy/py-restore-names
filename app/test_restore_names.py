import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_users,expected",
    [
        ([
            {"full_name": "John Doe", "first_name": None},
            {"full_name": "Jane Smith"},
            {"full_name": "Alice Wonderland", "first_name": "Alice"},
        ],
            [
            {"full_name": "John Doe", "first_name": "John"},
            {"full_name": "Jane Smith", "first_name": "Jane"},
            {"full_name": "Alice Wonderland", "first_name": "Alice"},
        ])
    ]
)
def test_restore_names(input_users: list[dict], expected: list[dict]) -> None:
    restore_names(input_users)
    assert input_users == expected
