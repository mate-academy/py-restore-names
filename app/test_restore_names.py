import pytest
from app.restore_names import restore_names


def test_restore_missing_first_name() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_restore_none_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    result = restore_names(users)
    assert result is None
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_dont_restore_existing_first_name() -> None:
    users = [
        {
            "first_name": "Jim",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Jim",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_empty_list_stays_empty() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_mixed_names() -> None:
    users = [
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
            "first_name": "Jim",
            "last_name": "Adams",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users == [
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
            "first_name": "Jim",
            "last_name": "Adams",
            "full_name": "Jack Holy",
        }
    ]


def test_dont_restore_empty_string_first_name() -> None:
    users = [
        {
            "first_name": "",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_restore_single_word_full_name() -> None:
    users = [
        {
            "last_name": "",
            "full_name": "Madonna",
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Madonna",
            "last_name": "",
            "full_name": "Madonna",
        }
    ]


def test_missing_first_name_with_empty_full_name_raises() -> None:
    users = [{"last_name": "", "full_name": ""}]
    with pytest.raises(IndexError):
        restore_names(users)
