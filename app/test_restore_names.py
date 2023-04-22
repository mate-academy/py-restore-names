import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template_without_first_name() -> list:
    return [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_first_name_not_in_users(user_template_without_first_name: list
                                 ) -> None:
    restore_names(user_template_without_first_name)
    assert user_template_without_first_name[0]["first_name"] == "Mike"


@pytest.fixture()
def user_template_first_name_none() -> list:
    return [{
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }]


def test_first_name_is_none(user_template_first_name_none: list) -> None:
    restore_names(user_template_first_name_none)
    assert user_template_first_name_none[0]["first_name"] == "Jack"
