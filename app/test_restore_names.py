import pytest
from app.restore_names import restore_names


def test_restore_only_missing_names() -> None:
    users = [{"last_name": "Adams", "full_name": "Mike Adams"}]
    restore_names(users)
    assert users == [{"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"}]


def test_restore_only_none_names() -> None:
    users = [{"first_name": None, "last_name": "Adams", "full_name": "Mike Adams"}]
    restore_names(users)
    assert users == [{"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"}]


