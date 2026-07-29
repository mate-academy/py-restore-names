import pytest
from app.restore_names import restore_names
from typing import List


@pytest.mark.parametrize(
    "list_before, list_changed", [
        (
            [{
                "full_name": "Cutie Patootie",
                "last_name": "Patootie",
                "first_name": None
            }],
            [{
                "full_name": "Cutie Patootie",
                "last_name": "Patootie",
                "first_name": "Cutie"
            }]
        ),
        (
            [{
                "full_name": "Fifa Fofi",
                "last_name": "Fofi",
            }],
            [{
                "full_name": "Fifa Fofi",
                "last_name": "Fofi",
                "first_name": "Fifa"
            }]
        ),
        (
            [{
                "full_name": "",
                "last_name": "",
                "first_name": ""
            }],
            [{
                "full_name": "",
                "last_name": "",
                "first_name": ""
            }]
        ),
        (
            [{
                "full_name": None,
                "first_name": "Boba"
            }],
            [{
                "full_name": None,
                "first_name": "Boba"
            }]
        )
    ]
)
def test_restore_names(
        list_before: List[dict],
        list_changed: List[dict]
) -> None:
    restore_names(list_before)
    assert list_before == list_changed
