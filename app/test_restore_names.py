import pytest
from app.restore_names import restore_names


def test_restore_name() -> None:
    initial_list = [
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
    expected_list = [
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

    restore_names(initial_list)
    assert (
        initial_list == expected_list
    ), "'restore_names' should correctly restore first names in initial list"
