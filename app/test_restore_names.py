import pytest
from app.restore_names import restore_names


@pytest.fixture
def users_none_first_name() -> list[dict]:
    return [
        {"first_name": None, "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"first_name": None, "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]


@pytest.fixture
def users_missing_first_name() -> list[dict]:
    return [
        {"last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]


@pytest.fixture
def users_existing_first_name() -> list[dict]:
    return [
        {"first_name": "Existing", "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"first_name": "Already", "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]


@pytest.fixture
def users_mixed() -> list[dict]:
    return [
        {"first_name": None, "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "Already", "last_name": "Smith",
         "full_name": "John Smith"},
    ]


def test_restore_none_first_name(users_none_first_name) -> None:
    restore_names(users_none_first_name)
    assert users_none_first_name[0]["first_name"] == "Jack"
    assert users_none_first_name[1]["first_name"] == "Mike"


def test_restore_missing_first_name(users_missing_first_name) -> None:
    restore_names(users_missing_first_name)
    assert users_missing_first_name[0]["first_name"] == "Jack"
    assert users_missing_first_name[1]["first_name"] == "Mike"


def test_first_name_already_exists(users_existing_first_name) -> None:
    restore_names(users_existing_first_name)
    assert users_existing_first_name[0]["first_name"] == "Existing"
    assert users_existing_first_name[1]["first_name"] == "Already"


def test_mixed_cases(users_mixed) -> None:
    restore_names(users_mixed)
    assert users_mixed[0]["first_name"] == "Jack"
    assert users_mixed[1]["first_name"] == "Mike"
    assert users_mixed[2]["first_name"] == "Already"
