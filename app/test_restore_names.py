import pytest
from app.restore_names import restore_names


@pytest.fixture()
def list_for_check() -> list:
    list_of_users = [
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
    return list_of_users


def test_should_check_first_name(list_for_check: list) -> None:
    restore_names(list_for_check)
    assert list_for_check[0]["first_name"] == "Jack"
    assert list_for_check[1]["first_name"] == "Mike"
