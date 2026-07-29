from typing import Any

import pytest
from app.restore_names import restore_names

full_name_data = [
    {"first_name": "Jack",
     "last_name": "Holy",
     "full_name": "Jack Holy"}
]


@pytest.fixture()
def name_template() -> list:
    person = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    return person


def test_check_none_name(name_template: Any) -> None:
    name_template[0]["first_name"] = None
    restore_names(name_template)
    assert name_template == full_name_data


def test_check_missed_name(name_template: Any) -> None:
    del name_template[0]["first_name"]
    restore_names(name_template)
    assert name_template == full_name_data
