import pytest
from app.restore_names import restore_names


@pytest.fixture()
def failed_database() -> list:
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


def test_if_first_name_is_none(failed_database: list) -> None:
    restore_names(failed_database)

    assert failed_database[0]["first_name"] == "Jack"


def test_if_dict_dont_have_first_name(failed_database: list) -> None:
    restore_names(failed_database)

    assert failed_database[1]["first_name"] == "Mike"
