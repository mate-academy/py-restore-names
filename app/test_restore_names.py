import pytest
from app.restore_names import restore_names


@pytest.fixture()
def first_name_is_none() -> list:
    user = [{"first_name": None,
             "last_name": "Holy",
             "full_name": "Jack Holy",
             }]
    return user


@pytest.fixture()
def absence_of_first_name() -> list:
    user = [{"last_name": "Adams",
             "full_name": "Mike Adams",
             }]
    return user


def test_first_name_is_none(first_name_is_none: list) -> None:
    restore_names(first_name_is_none)
    assert first_name_is_none[0]["first_name"] == "Jack"


def test_absence_of_first_name(absence_of_first_name: list) -> None:
    restore_names(absence_of_first_name)
    assert absence_of_first_name[0]["first_name"] == "Mike"
