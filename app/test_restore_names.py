import pytest
from app.restore_names import restore_names


@pytest.fixture()
def person_template() -> list[dict]:
    return [
        {
            "first_name": "Test",
            "last_name": "Testekno",
            "full_name": "Test Testekno"
        }
    ]


def test_can_restore_first_name(
        person_template: list[dict]) -> None:
    person_template[0]["first_name"] = None
    restore_names(person_template)
    expected_result = person_template[0]["full_name"].split()[0]
    assert person_template[0]["first_name"] == expected_result


def test_can_restore_first_name_if_there_is_no_dict(
        person_template: list[dict]) -> None:
    del person_template[0]["first_name"]
    restore_names(person_template)
    expected_result = person_template[0]["full_name"].split()[0]
    assert person_template[0]["first_name"] == expected_result
