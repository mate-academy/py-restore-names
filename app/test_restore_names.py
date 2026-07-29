import pytest

from app.restore_names import restore_names


@pytest.fixture()
def users_info() -> list:
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


def test_restore_names(users_info: list) -> None:
    restore_names(users_info)
    assert users_info[0]["first_name"] == "Jack"
    assert users_info[1]["first_name"] == "Mike"
