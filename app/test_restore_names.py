import pytest
from app.restore_names import restore_names


@pytest.fixture()
def generate_user_with_first_name_none() -> list[dict]:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


@pytest.fixture()
def generate_user_without_first_name() -> list[dict]:
    return [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_restore_name_if_user_first_name_is_none(
        generate_user_with_first_name_none: list[dict]) -> None:
    restore_names(generate_user_with_first_name_none)
    assert generate_user_with_first_name_none[0]["first_name"] == "Jack"


def test_restore_name_if_user_without_first_name(
        generate_user_without_first_name: list[dict]) -> None:
    restore_names(generate_user_without_first_name)
    assert generate_user_without_first_name[0]["first_name"] == "Mike"
