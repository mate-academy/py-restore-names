import pytest
from typing import List, Dict

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_first_names",
    [
        (
            [{"full_name": "Jack Holy"}, {"full_name": "Mike Adams"}],
            ["Jack", "Mike"],
        ),
        (
            [
                {"first_name": None, "full_name": "Jack Holy"},
                {"first_name": None, "full_name": "Mike Adams"},
            ],
            ["Jack", "Mike"],
        ),
    ],
)
def test_restore_names_missing_or_none_first_nam(
    users: List[Dict], expected_first_names: List[str]
) -> None:
    restore_names(users)
    for i in range(len(users)):
        assert users[i]["first_name"] == expected_first_names[i]
