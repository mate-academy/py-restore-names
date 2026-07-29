import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            [
                {"first_name": None, "last_name": "Holy",
                 "full_name": "Jack Holy"},
                {"last_name": "Adams", "full_name": "Mike Adams"},
            ],
            [
                {"first_name": "Jack", "last_name": "Holy",
                 "full_name": "Jack Holy"},
                {"first_name": "Mike", "last_name": "Adams",
                 "full_name": "Mike Adams"},
            ],
        ),
        (
            [
                {"first_name": "Alice", "last_name": "Wonder",
                 "full_name": "Alice Wonder"},
                {"first_name": "Bob", "last_name": "Builder",
                 "full_name": "Bob Builder"},
            ],
            [
                {"first_name": "Alice", "last_name": "Wonder",
                 "full_name": "Alice Wonder"},
                {"first_name": "Bob", "last_name": "Builder",
                 "full_name": "Bob Builder"},
            ],
        ),
        (
            [
                {"first_name": "Charlie", "last_name": "Chaplin",
                 "full_name": "Charlie Chaplin"},
                {"first_name": None, "last_name": "Doe",
                 "full_name": "Jane Doe"},
                {"last_name": "Smith", "full_name": "John Smith"},
            ],
            [
                {"first_name": "Charlie", "last_name": "Chaplin",
                 "full_name": "Charlie Chaplin"},
                {"first_name": "Jane", "last_name": "Doe",
                 "full_name": "Jane Doe"},
                {"first_name": "John", "last_name": "Smith",
                 "full_name": "John Smith"},
            ],
        ),

        (
            [
                {"first_name": None, "last_name": "Jones",
                 "full_name": "  Harry Jones  "},
            ],
            [
                {"first_name": "Harry", "last_name": "Jones",
                 "full_name": "  Harry Jones  "},
            ],
        ),
    ],
)
def test_restore_names(input_data: list, expected_output: list) -> None:
    restore_names(input_data)
    assert input_data == expected_output
