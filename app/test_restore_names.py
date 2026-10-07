import pytest
from app.restore_names import restore_names


User: type[dict[str, str | None]] = dict[str, str | None]


@pytest.fixture()
def user_fixture() -> list:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": None,
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_if_first_name_is_none(user_fixture: list) -> None:
    restore_names(user_fixture)
    assert user_fixture[0]["first_name"] == "Jack"
    assert user_fixture[1]["first_name"] == "Mike"


def test_if_first_name_is_missing(user_fixture: list) -> None:
    del user_fixture[0]["first_name"]
    del user_fixture[1]["first_name"]
    restore_names(user_fixture)
    assert user_fixture[0]["first_name"] == "Jack"
    assert user_fixture[1]["first_name"] == "Mike"


def test_name_restoration(user_fixture: list) -> None:
    restore_names(user_fixture)
    assert user_fixture[0]["first_name"] == "Jack"
    assert user_fixture[1]["first_name"] == "Mike"


def test_no_modification_if_first_name_exists(user_fixture: list) -> None:
    user_fixture[0]["first_name"] = "John"
    user_fixture[1]["first_name"] = "David"
    restore_names(user_fixture)
    assert user_fixture[0]["first_name"] == "John"
    assert user_fixture[1]["first_name"] == "David"


def test_restore_names_returns_none(user_fixture: list) -> None:
    result: None = restore_names(user_fixture)
    assert result is None
