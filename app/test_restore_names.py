from typing import List
import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("users,expected", [
    (
        [{"first_name": None, "full_name": "Jack Holly"}],
        [{"first_name": "Jack", "full_name": "Jack Holly"}],
    ),
    (
        [{"full_name": "Mike Adams"}],
        [{"first_name": "Mike", "full_name": "Mike Adams"}]
    ),
])
def test_restore_names(users: List[dict], expected: List[dict]) -> None:
    restore_names(users)
    assert users == expected
