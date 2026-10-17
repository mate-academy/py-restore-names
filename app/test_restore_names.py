import pytest
from app.restore_names import restore_names


@pytest.fixture()
def db_template() -> list:
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


def test_restored_first_name_in_list(db_template: list) -> None:
    restore_names(db_template)
    for user in db_template:
        assert "first_name" in user


def test_restored_first_name_value_in_list(db_template: list) -> None:
    restore_names(db_template)
    for user in db_template:
        assert user["first_name"] is not None


def test_name_should_not_be_empty_string(db_template: list) -> None:
    restore_names(db_template)
    for user in db_template:
        assert user["first_name"] != ""
