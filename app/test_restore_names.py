import pytest
from app.restore_names import restore_names
from typing import List, Dict


@pytest.mark.parametrize(
    "input_data, expected_first_name",
    [
        (
            {"first_name": None,
             "last_name": "Holy",
             "full_name": "Jack Holy"},
            "Jack"
        ),
        (
            {"last_name": "Adams",
             "full_name": "Mike Adams"},
            "Mike",
        ),
    ]
)
def test_restore_names(input_data: Dict[str, str],
                       expected_first_name: str) -> None:
    users: List[Dict[str, str]] = [input_data]
    restore_names(users)
    assert users[0]["first_name"] == expected_first_name
