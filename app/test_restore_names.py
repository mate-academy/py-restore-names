from copy import deepcopy
import app.restore_names as restore_module


def test_restore_missing_first_name_key() -> None:
    users = [{"last_name": "Smith", "full_name": "John Smith"}]
    restore_module.restore_names(users)
    assert users[0]["first_name"] == "John"
    assert users[0]["last_name"] == "Smith"
    assert users[0]["full_name"] == "John Smith"


def test_restore_none_first_name() -> None:
    users = [{"first_name": None, "last_name": "Doe", "full_name": "Jane Doe"}]
    restore_module.restore_names(users)
    assert users[0]["first_name"] == "Jane"
    assert users[0]["last_name"] == "Doe"
    assert users[0]["full_name"] == "Jane Doe"


def test_do_not_overwrite_existing_first_name() -> None:
    users = [{"first_name": "Alice", "last_name": "Wonderland",
              "full_name": "Alice Wonderland"}]
    before = deepcopy(users)
    restore_module.restore_names(users)
    assert users == before


def test_full_name_with_extra_spaces() -> None:
    users = [{"first_name": None, "last_name": "Brown",
              "full_name": "   Charlie   Brown  "}]
    restore_module.restore_names(users)
    assert users[0]["first_name"] == "Charlie"
    assert users[0]["last_name"] == "Brown"


def test_full_name_single_name() -> None:
    users = [{"first_name": None, "last_name": "", "full_name": "Madonna"}]
    restore_module.restore_names(users)
    assert users[0]["first_name"] == "Madonna"
    assert users[0]["last_name"] == ""


def test_empty_list_no_error() -> None:
    users: list[dict] = []
    restore_module.restore_names(users)
    assert users == []


def test_multiple_users_mix() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "Eve", "last_name": "Stone", "full_name": "Eve Stone"},
    ]
    restore_module.restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Eve"