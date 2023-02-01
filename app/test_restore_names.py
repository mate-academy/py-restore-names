import pytest
from app.restore_names import restore_names


def test_positive_scenario() -> None:
    input_users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    expected = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(input_users)
    assert input_users == expected


def test_error() -> None:
    with pytest.raises(KeyError):
        restore_names([{}])


def test_empty_array() -> None:
    input_users = []
    restore_names([])
    assert input_users == []
