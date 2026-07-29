from typing import List, Dict, Any
import pytest
from app.restore_names import restore_names

# write your tests here


@pytest.mark.parametrize(
    "users,expected_first_names",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            ["Jack", "Mike"]
        ),
        (
            [
                {
                    "first_name": "Already",
                    "last_name": "Known",
                    "full_name": "Already Known",
                }
            ],
            ["Already"]
        ),
        (
            [
                {
                    "full_name": "SingleName",
                }
            ],
            ["SingleName"]
        ),
    ]
)
def test_restore_names(
    users: List[Dict[str, Any]],
    expected_first_names: List[str]
) -> None:
    restore_names(users)
    for i in range(len(users)):
        assert users[i]["first_name"] == expected_first_names[i]
