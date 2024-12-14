import pytest
from app.restore_names import restore_names
from typing import Dict

# write your tests here


@pytest.fixture()
def person_template() -> Dict[str, str]:
    return {"first_name": "Illya",
            "last_name": "Kovalevskaya",
            "full_name": "Illya Kovalevskaya"}


def test_restore_names_if_firstname_is_none(person_template: Dict[str, str])\
        -> None:
    person_template["first_name"] = None
    restore_names([person_template])
    assert person_template["first_name"] == "Illya"


def test_restore_names_if_name_is_missing(person_template: Dict[str, str]) \
        -> None:
    person_template["first_name"] = " "
    restore_names([person_template])
    assert person_template["first_name"] == " "
