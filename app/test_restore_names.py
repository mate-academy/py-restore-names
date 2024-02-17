import pytest
from app.restore_names import restore_names


@pytest.fixture
def users_with_missing_first_names() -> None:
    return [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]


@pytest.fixture
def users_with_complete_data() -> None:
    return [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike",
         "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]


def test_restore_names_with_missing_first_names() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    expected = [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike",
         "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users == expected


def test_restore_names_exis_f_names(users_with_complete_data: None) -> None:
    original_data = users_with_complete_data.copy()
    restore_names(users_with_complete_data)
    assert users_with_complete_data == original_data


def test_restore_names_with_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_names_handles_multiple_names_correctly() -> None:
    users = [{"last_name": "Smith", "full_name": "John Alex Smith"}]
    restore_names(users)
    assert users == [{"first_name": "John",
                      "last_name": "Smith",
                      "full_name": "John Alex Smith"}]
