from __future__ import annotations
import pytest
from app.restore_names import restore_names


@pytest.fixture()
def people_template() -> list:
    people = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"}]
    return people


def test_first_name_is_none(people_template: people_template) -> None:
    restore_names(people_template)
    assert people_template[0]["first_name"] == "Jack"
    assert people_template[1]["first_name"] == "Mike"
