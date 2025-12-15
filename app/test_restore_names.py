import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_data() -> list:
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


def test_first_name_should_be_taken_if_none_or_empty(
        user_data: list
) -> None:
    restore_names(user_data)

    assert user_data[0]["first_name"] == "Jack"
    assert user_data[1]["first_name"] == "Mike"
