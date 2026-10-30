import pytest
from app.restore_names import restore_names


@pytest.fixture()
def no_name_person_template() -> dict[str, str]:
    return {
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }


@pytest.fixture()
def name_person_template() -> dict[str, str]:
    return {
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }


def test_restore_name_if_no_name_field(no_name_person_template: dict[str, str],
                                       name_person_template: dict[str, str]) \
        -> None:
    restore_names([no_name_person_template])

    assert no_name_person_template == name_person_template


def test_restore_name_if_none(no_name_person_template: dict[str, str],
                              name_person_template: dict[str, str]) -> None:
    no_name_person_template["first_name"] = None

    restore_names([no_name_person_template])

    assert no_name_person_template == name_person_template
