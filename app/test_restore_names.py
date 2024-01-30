import pytest
from app.restore_names import restore_names

@pytest.fixture()
def user_example():
    user = [{"first_name": None, "full_name": "John Smith"},
            {"full_name": "Matt Jackson"}]
    return user


def test_restore_names_with_none_name(user_example):
    restore_names(user_example)
    assert user_example == [{"first_name": "John", "full_name": "John Smith"},
            {"first_name": "Matt", "full_name": "Matt Jackson"}]
