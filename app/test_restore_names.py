import pytest
from app.restore_names import restore_names

from typing import Dict


@pytest.fixture()
def person_template() -> Dict[str, str]:
    return {
        "first_name": None,
        "last_name": "Scofield",
        "full_name": "Michael Scofield"
    }


def test_restore_names_if_firstname_is_missing(
        person_template: Dict[str, str]
) -> None:
    del person_template["first_name"]
    restore_names([person_template])
    assert person_template["first_name"] == "Michael"


def test_restore_names_if_firstname_is_none(
        person_template: Dict[str, str]
) -> None:
    person_template["first_name"] = None
    restore_names([person_template])
    assert person_template["first_name"] == "Michael"
