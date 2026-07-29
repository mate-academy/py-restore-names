import pytest
from app.restore_names import restore_names


@pytest.fixture()
def person_template() -> list[dict]:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_should_add_name_when_name_none(person_template: list) -> None:
    user = person_template
    restore_names(user)

    assert user[0]["first_name"] == "Jack"


def test_should_add_name_when_name_is_not_user(person_template: list) -> None:
    user = person_template
    restore_names(user)

    assert user[1]["first_name"] == "Mike"
