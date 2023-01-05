from app.restore_names import restore_names
import pytest


@pytest.fixture()
def list_none_template() -> list:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


@pytest.fixture()
def list_missed_template() -> list:
    return [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_first_name_none(list_none_template: list) -> None:
    restore_names(list_none_template)
    assert list_none_template == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_first_name_missed(list_missed_template: list) -> None:
    restore_names(list_missed_template)
    assert list_missed_template == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
