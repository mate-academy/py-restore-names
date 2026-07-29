import pytest

from app.restore_names import restore_names


@pytest.fixture
def users_list_template() -> list:
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


def test_first_name_none(users_list_template: list)\
        -> None:
    users = users_list_template
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_no_first_name_key(users_list_template: list)\
        -> None:
    users = users_list_template
    restore_names(users)
    assert "first_name" in users[1].keys()


def test_all_data_correct(users_list_template: list) \
        -> None:
    users = users_list_template
    users[0]["first_name"] = "Jack"
    users[1]["first_name"] = "Mike"
    restore_names(users)
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]
