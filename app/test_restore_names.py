from typing import List
import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        (
            [
                {"first_name": None,
                 "last_name": "Holy",
                 "full_name": "Jack Holy", },
                {"last_name": "Adams",
                 "full_name": "Mike Adams", },
                {"first_name": "No",
                 "last_name": "Any",
                 "full_name": "Changes", },
            ],
            [
                {"first_name": "Jack",
                 "last_name": "Holy",
                 "full_name": "Jack Holy", },
                {"first_name": "Mike",
                 "last_name": "Adams",
                 "full_name": "Mike Adams", },
                {"first_name": "No",
                 "last_name": "Any",
                 "full_name": "Changes", },
            ]
        )
    ]
)
def test_restore_names(users: List[dict], expected: List[dict]) -> None:
    restore_names(users)
    assert users == expected
