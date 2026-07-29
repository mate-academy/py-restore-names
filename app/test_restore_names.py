import pytest
from app.restore_names import restore_names


def test_restore_missing_first_name() -> None:
    users = [{"first_name": None,
              "full_name": "Jack Holy",
              "last_name": "Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_check_first_name_in_list() -> None:
    users = [{"first_name": "Jack", "full_name": "Holy", "last_name": "Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_check_last_name_have_more_words() -> None:
    users = [{"full_name": "John Ronald Reuel Tolkien", "last_name": "Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_check_first_name_in_list_none() -> None:
    users = [{"first_name": None,
              "full_name": "Jack Holy",
              "last_name": "Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_check_last_name_is_none() -> None:
    users = [{"full_name": None, "last_name": "Holy"}]
    with pytest.raises(AttributeError):
        restore_names(users)
