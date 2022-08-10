import pytest
from app.restore_names import restore_names


@pytest.fixture
def users():
    return [{
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy",
    },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


@pytest.fixture
def result_users():
    return [
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


def test_should_raise_exception_if_parameter_not_list():
    with pytest.raises(TypeError):
        restore_names(({"Firstname": "Oliver"}))


def test_should_restore_names(users, result_users):
    restore_names(users)
    assert users == result_users
