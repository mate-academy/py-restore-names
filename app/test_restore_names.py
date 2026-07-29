import pytest

from app.restore_names import restore_names


@pytest.fixture
def list_of_users() -> list:
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
        {
            "first_name": "Johny",
            "last_name": "Molly",
            "full_name": "Johny Molly",
        }
    ]


def test_restore_names(list_of_users: list) -> None:
    restore_names(list_of_users)
    assert list_of_users[0]["first_name"] == "Jack"
    assert list_of_users[1]["first_name"] == "Mike"
    assert list_of_users[2]["first_name"] == "Johny"
