import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user, expected_name",
    [
        ({"first_name": None, "full_name": "Jack Holy"}, "Jack"),
        ({"full_name": "Mike Adams"}, "Mike"),
        ({"first_name": "Mike", "full_name": "Jack Holy"}, "Mike"),
    ],
)
def test_restore_names(user: dict, expected_name: str) -> None:
    restore_names([user])
    assert user["first_name"] == expected_name


def test_restore_names_multiple_users() -> None:
    users = [
        {"first_name": None, "full_name": "Jack Holy"},
        {"full_name": "Mike Adams"},
        {"first_name": "Ann", "full_name": "Kate Smith"},
    ]

    restore_names(users)

    assert [user["first_name"] for user in users] == ["Jack", "Mike", "Ann"]


def test_restore_names_empty_list() -> None:
    users = []

    restore_names(users)

    assert users == []


def test_restore_names_returns_none() -> None:
    users = [{"first_name": None, "full_name": "Jack Holy"}]

    assert restore_names(users) is None
