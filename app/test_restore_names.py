import pytest
from app.restore_names import restore_names

# write your tests here



@pytest.fixture()
def person_template():
    return {"first_name": "Illya",
        "last_name":"Kovaliuk",
        "full_name":"Illya Kovaliuk"}
def test_restore_names_if_firstname_is_None(person_template):
    person_template["first_name"] = None
    assert person_template["first_name"] is None


def test_restore_names_if_firstname_is_missing(person_template):
    person_template["first_name"] = ""
    assert person_template["first_name"] is ""