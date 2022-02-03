import copy
from app.restore_names import restore_names


def test_return_none():
    assert restore_names([{
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }]) is None


def test_without_restore():
    values = [
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
    ]
    values_for_test = copy.deepcopy(values)
    restore_names(values_for_test)
    assert values == values_for_test


def test_with_restore():
    values = [
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
    ]
    values_for_test = copy.deepcopy(values)
    restore_names(values_for_test)
    assert expected == values_for_test
