import pytest
from app.restore_names import restore_names


@pytest.fixture(scope="module")
def prepare_users() -> list:
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
    ]
    return users


def test_first_name_is_none(prepare_users: list) -> None:
    restore_names(prepare_users)
    assert (
        prepare_users[0]["first_name"]
        == prepare_users[0]["full_name"].split()[0]
    )


def test_first_name_not_in_user(prepare_users: list) -> None:
    restore_names(prepare_users)
    assert (
        prepare_users[1]["first_name"]
        == prepare_users[1]["full_name"].split()[0]
    )
