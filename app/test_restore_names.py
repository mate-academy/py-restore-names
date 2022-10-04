import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_without_first_name_field():
    yield [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


@pytest.fixture()
def user_with_first_name_none():
    yield [
        {
            "first_name": None,
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_without_field(user_without_first_name_field):
    restore_names(user_without_first_name_field)

    assert (
        user_without_first_name_field[0]["first_name"] ==
        user_without_first_name_field[0]["full_name"].split()[0]
    )


def test_name_field_is_none(user_with_first_name_none):
    restore_names(user_with_first_name_none)

    assert (
        user_with_first_name_none[0]["first_name"] ==
        user_with_first_name_none[0]["full_name"].split()[0]
    )
