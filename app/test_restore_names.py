import pytest

from app.restore_names import restore_names


@pytest.fixture()
def user_template():
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_restore_names_when_none(user_template):
    restore_names([user_template[0]])
    assert [user_template[0]] == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_restore_names_when_missing_first_name(user_template):
    restore_names([user_template[1]])
    assert [user_template[1]] == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
