import pytest  # noqa: F401
from app.restore_names import restore_names


def test_if_first_name_none() -> None:
    list_for_test = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    result = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(list_for_test)

    assert list_for_test == result


def test_if_dict_without_first_name() -> None:
    list_for_test = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]

    result = [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]

    restore_names(list_for_test)

    assert list_for_test == result


def test_default_dict() -> None:
    list_for_test = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    result = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(list_for_test)

    assert list_for_test == result


def test_list_without_dicts() -> None:
    list_for_test = []

    result = []

    restore_names(list_for_test)

    assert list_for_test == result
