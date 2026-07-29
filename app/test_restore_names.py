import pytest
from app.restore_names import restore_names


@pytest.fixture
def input_user_template():
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


def test_first_name_with_none_value(input_user_template):
    restore_names(input_user_template)
    assert input_user_template[0]["first_name"] == "Jack"


def test_first_name_without_key(input_user_template):
    restore_names(input_user_template)
    assert input_user_template[1]["first_name"] == "Mike"
