from typing import List, Dict

import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users", [
        pytest.param(
            [{
                "last_name": "Adams",
                "full_name": "Mike Adams"
            }],
            id="no name record present"
        ),
        pytest.param(
            [{
                "first_name": None,
                "last_name": "Adams",
                "full_name": "Mike Adams"
            }],
            id="name value is None"
        ),
        pytest.param(
            [{
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams"
            }],
            id="name value is correct"
        )
    ]
)
def test_restore_name(users: List[Dict[str, str]]) -> None:
    restore_names(users)
    assert users == [{
        "first_name": "Mike",
        "last_name": "Adams",
        "full_name": "Mike Adams"
    }]
