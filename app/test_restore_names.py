import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            [{"full_name": "Alice Smith"}],
            [{"full_name": "Alice Smith", "first_name": "Alice"}]
        ),
        (
            [{"full_name": "Bob Johnson", "first_name": None}],
            [{"full_name": "Bob Johnson", "first_name": "Bob"}]
        ),
        (
            [{"full_name": "Carol White", "first_name": "Carol"}],
            [{"full_name": "Carol White", "first_name": "Carol"}]
        ),
        (
            [{"full_name": "David Lee", "first_name": "Dave"}],
            [{"full_name": "David Lee", "first_name": "Dave"}]
        ),
        (
            [
                {"full_name": "Eve Adams"},
                {"full_name": "Frank Moore", "first_name": None},
                {"full_name": "Grace Kim", "first_name": "Grace"}
            ],
            [
                {"full_name": "Eve Adams", "first_name": "Eve"},
                {"full_name": "Frank Moore", "first_name": "Frank"},
                {"full_name": "Grace Kim", "first_name": "Grace"}
            ]
        )
    ])
def test_restore_name_function(input_data: list, expected: list) -> None:
    restore_names(input_data)
    assert input_data == expected
