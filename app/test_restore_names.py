import pytest
from app.restore_names import restore_names

@pytest.mark.parametrize(
    "users, expected_first_names",
    [
        (
            [{"full_name": "Alice Wonderland"}],
            ["Alice"],
        ),
        (
            [{"first_name": None, "full_name": "John Doe"}],
            ["John"],
        ),
        (
            [{"first_name": "Jane", "full_name": "Jane Smith"}],
            ["Jane"],  # не змінюється
        ),
        (
            [
                {"full_name": "Tom Sawyer"},
                {"first_name": None, "full_name": "Huck Finn"},
                {"first_name": "Polly", "full_name": "Aunt Polly"},
            ],
            ["Tom", "Huck", "Polly"],
        ),
    ],
)
def test_restore_names(users, expected_first_names):
    restore_names(users)
    result = [u["first_name"] for u in users]
    assert result == expected_first_names
