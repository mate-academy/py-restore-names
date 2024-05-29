import pytest
from app.restore_names import restore_names


@pytest.fixture()
def prepare_test_users() -> list[dict]:
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
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]
    return users


def test_restore_names(prepare_test_users: list[dict]) -> None:
    restore_names(prepare_test_users)
    assert prepare_test_users == [
        {"first_name": "Jack", "last_name":
            "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name":
            "Mike Adams", "first_name": "Mike"},
        {"first_name": "Jack", "last_name":
            "Holy", "full_name": "Jack Holy"}
    ]
