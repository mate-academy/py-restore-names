import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("test_input, expected", [
    ([
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
        {"first_name": "Jane", "last_name": "Smith", "full_name": "Jane Smith"}
    ], [
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
        {"first_name": "Jane", "last_name": "Smith", "full_name": "Jane Smith"}
    ]),
    ([
        {"last_name": "Doe", "full_name": "John Doe"},
        {"first_name": None, "last_name": "Smith", "full_name": "Jane Smith"}
    ], [
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
        {"first_name": "Jane", "last_name": "Smith", "full_name": "Jane Smith"}
    ]),
    ([
        {"last_name": "Doe", "full_name": "John Doe"},
        {"last_name": "Smith", "full_name": "Jane Smith"}
    ], [
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
        {"first_name": "Jane", "last_name": "Smith", "full_name": "Jane Smith"}
    ])
])
def test_restore_names(test_input: list, expected: list) -> None:
    restore_names(test_input)
    assert test_input == expected
