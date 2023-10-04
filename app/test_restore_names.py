import pytest
from app.restore_names import restore_names


@pytest.fixture()
def jack_template_before() -> dict:
    yield {
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }


@pytest.fixture()
def jack_template_after() -> dict:
    yield {
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }


def test_first_name_empty(
        jack_template_before: dict,
        jack_template_after: dict
) -> None:
    users = [jack_template_before]
    restore_names(users)
    assert users == [jack_template_after]


def test_first_name_restored_if_was_none(
        jack_template_before: dict,
        jack_template_after: dict
) -> None:
    jack_template_before["first_name"] = None
    users = [jack_template_before]
    restore_names(users)
    assert users == [jack_template_after]


def test_restores_two_names(
        jack_template_before: dict,
        jack_template_after: dict
) -> None:
    mike_before = {
        "first_name": None,
        "last_name": "Adams",
        "full_name": "Mike Adams"
    }
    mike_after = {
        "first_name": "Mike",
        "last_name": "Adams",
        "full_name": "Mike Adams"
    }
    users = [mike_before, jack_template_before]
    restore_names(users)
    assert users == [mike_after, jack_template_after]
