import copy
from app.restore_names import restore_names


def test_with_first_name() -> None:
    names = [
        {
            "first_name": "Jenny",
            "last_name": "Holy",
            "full_name": "Jenny Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    expected = copy.deepcopy(names)
    restore_names(names)
    assert names == expected


def test_with_first_name_and_without() -> None:
    names = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jenny Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    expected = [
        {
            "first_name": "Jenny",
            "last_name": "Holy",
            "full_name": "Jenny Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    restore_names(names)
    assert names == expected


def test_without_firstnames() -> None:
    names = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jenny Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    expected = [
        {
            "first_name": "Jenny",
            "last_name": "Holy",
            "full_name": "Jenny Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    restore_names(names)
    assert names == expected
