import pytest
from app.restore_names import restore_names


@pytest.fixture
def users_fixture() -> list:
    return [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_restore_names_no_first_name(users_fixture: list) -> None:
    restore_names(users_fixture)
    assert users_fixture[0]["first_name"] == "Jack"
    assert users_fixture[1]["first_name"] == "Mike"


def test_restore_names_when_first_name_is_none(users_fixture: list) -> None:
    users_fixture[0]["first_name"] = None
    restore_names(users_fixture)
    assert users_fixture[0]["first_name"] == "Jack"
