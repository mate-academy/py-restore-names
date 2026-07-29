import pytest
from app.restore_names import restore_names


@pytest.fixture()
def person_template() -> list:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_with_name_none(person_template: list) -> None:
    restore_names(person_template)
    expected = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    assert person_template == expected


def test_with_name(person_template: list) -> None:
    person_template[0]["first_name"] = "Jack"
    person_template[1]["first_name"] = "Mike"
    restore_names(person_template)
    expected = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    assert person_template == expected
