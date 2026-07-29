import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_template():
    users = [
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
    return users


def test_correct_first_name(users_template):
    restore_names(users_template)
    assert users_template == [
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


def test_return_none(users_template):
    assert restore_names(users_template) is None


def test_type_error():
    with pytest.raises(TypeError):
        restore_names("test_error")


def test_empty_list(users_template):
    users_template = []
    restore_names(users_template)
    assert users_template == []
