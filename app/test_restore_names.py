from typing import Dict

import pytest
from app.restore_names import restore_names


@pytest.fixture()
def person_template() -> Dict:
    return {
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }


def test_restore_names_if_first_name_is_none(
        person_template: Dict[str, str]
) -> None:
    person_template["first_name"] = None
    restore_names([person_template])
    assert person_template["first_name"] == "Jack"


def test_restore_names_if_not_first_name(
        person_template: Dict[str, str]
) -> None:
    del person_template["first_name"]
    restore_names([person_template])
    assert person_template["first_name"] == "Jack"
