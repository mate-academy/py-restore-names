import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_first_name_is_none() -> list:
    yield [
        {
            "first_name": None,
            "last_name": "Jordan",
            "full_name": "Mike Jordan"
        },
        {
            "first_name": None,
            "last_name": "Mask",
            "full_name": "Ilon Mask"
        },

    ]


@pytest.fixture()
def user_not_have_first_name() -> list:
    yield [
        {
            "last_name": "Jordan",
            "full_name": "Mike Jordan"
        },
        {
            "last_name": "China",
            "full_name": "Misha China"
        },
    ]


def test_first_name_is_none(user_first_name_is_none: list) -> None:
    restore_names(user_first_name_is_none)
    assert user_first_name_is_none[0]["first_name"]
    assert user_first_name_is_none[1]["first_name"]


def test_first_name_not_exist(user_not_have_first_name: list) -> None:
    restore_names(user_not_have_first_name)
    assert user_not_have_first_name[0]["first_name"]
    assert user_not_have_first_name[1]["first_name"]
