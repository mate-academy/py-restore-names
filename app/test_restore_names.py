import pytest
from app.restore_names import restore_names


@pytest.fixture()
def prepare_test_users() -> list[dict]:
    users = [
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "John Smith"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
        {
            "first_name": "Johny",
            "last_name": "Dep",
            "full_name": "Johny Dep"
        }
    ]
    return users


def test_restore_names(prepare_test_users: list[dict]) -> None:
    restore_names(prepare_test_users)
    assert prepare_test_users == [
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "John Smith"
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
        {
            "first_name": "Johny",
            "last_name": "Dep",
            "full_name": "Johny Dep"
        }
    ]
