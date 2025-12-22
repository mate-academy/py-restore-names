import pytest
from app.restore_names import restore_names


def test_add_name_when_none() -> None:
    users = [{
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }]
    restore_names(users)
    assert users == [{
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }]


def test_do_nothing_when_empty() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_add_name_when_not_existing() -> None:
    users = [{
        "last_name": "Adams",
        "full_name": "Mike Adams"
    }]
    restore_names(users)
    assert users == [{
        "first_name": "Mike",
        "last_name": "Adams",
        "full_name": "Mike Adams"
    }]


def test_not_rename_if_name_exists() -> None:
    users = [{
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }]
    restore_names(users)
    assert users == [{
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }]


def test_should_take_first_name_when_no_lastname_in_full_name() -> None:
    users = [{
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack"
    }]
    restore_names(users)
    assert users == [{
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack"
    }]


def test_should_raise_key_error() -> None:
    with pytest.raises(KeyError):
        restore_names([{}])
