from typing import Any
import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "name,expected",
    [
        (
            [{"first_name": None, "full_name": "Mike Adams"}],
            [{"first_name": "Mike", "full_name": "Mike Adams"}]
        ),
        (
            [{"full_name": "Mike Adams"}],
            [{"first_name": "Mike", "full_name": "Mike Adams"}]
        )
    ]
)
def test_of_first_name(name: Any, expected: Any) -> None:
    restore_names(name)
    assert name == expected
