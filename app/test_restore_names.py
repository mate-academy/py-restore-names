import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user() -> list:
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


def test_should_restore_name(user: list) -> None:
    restore_names(user)
    assert user[0]["first_name"] == "Jack"
    assert user[1]["first_name"] == "Mike"
