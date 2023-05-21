import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_dictionary() -> dict:
    yield [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]


@pytest.fixture()
def another_user_dictionary() -> dict:
    yield [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_restore_names_function(
        user_dictionary: dict,
        another_user_dictionary: dict
) -> None:
    restore_names(user_dictionary)
    restore_names(another_user_dictionary)
    assert user_dictionary[0]["first_name"] == "Jack"
    assert another_user_dictionary[0]["first_name"] == "Mike"
