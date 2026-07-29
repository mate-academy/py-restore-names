import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_information() -> list:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holly"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]


def test_restore_names(
        users_information: list
) -> None:
    restore_names(users_information)
    assert users_information[0]["first_name"] == "Jack"
    assert users_information[1]["first_name"] == "Mike"
