import pytest
from app.restore_names import restore_names
from typing import Dict


@pytest.fixture()
def person_template() -> Dict[str, str]:
    return {"first_name": "Bob",
            "last_name": "Smith",
            "full_name": "Bob Smith"}


def test_restore_names_if_firstname_is_none(
        person_template: Dict[str, str]) -> None:
    person_template["first_name"] = None
    restore_names([person_template])
    assert person_template["first_name"] == "Bob"


def test_restore_names_if_firstname_is_missing(
        person_template: Dict[str, str]) -> None:
    del person_template["first_name"]
    restore_names([person_template])
    assert person_template["first_name"] == "Bob"


def test_restore_names_if_firstname_is_present(
        person_template: Dict[str, str]) -> None:
    restore_names([person_template])
    assert person_template["first_name"] == "Bob"


def test_restore_names_if_fullname_has_multiple_words() -> None:
    user = {"last_name": "Smith", "full_name": "Robert John Smith"}
    restore_names([user])
    assert user["first_name"] == "Robert"


def test_restore_names_if_fullname_has_one_word() -> None:
    user = {"last_name": "Smith", "full_name": "Robert"}
    restore_names([user])
    assert user["first_name"] == "Robert"
