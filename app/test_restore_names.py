import pytest

from typing import List

from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> List[dict]:
    return [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


@pytest.fixture()
def expected_template() -> dict:
    return {
        "first_name": "Mike",
        "last_name": "Adams",
        "full_name": "Mike Adams",
    }


def test_should_restore_name_when_name_is_missing(
        users_template: List[dict],
        expected_template: dict
) -> None:
    user = users_template[0]
    restore_names(users_template)
    assert user == expected_template


def test_should_restore_name_when_name_is_none(
        users_template: List[dict],
        expected_template: dict
) -> None:
    user = users_template[0]
    user["first_name"] = None

    restore_names(users_template)
    assert user == expected_template


def test_should_not_restore_name_when_name_is_correct(
        users_template: List[dict],
        expected_template: dict
) -> None:
    user = users_template[0]
    user["first_name"] = "Mike"

    restore_names(users_template)
    assert user == expected_template
