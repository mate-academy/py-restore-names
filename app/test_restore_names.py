import pytest
from app import restore_names


@pytest.mark.parametrize(
    "user, expected_first_name",
    [
        pytest.param(
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            "Jack",
            id="first_name is None",
        ),
        pytest.param(
            {"last_name": "Adams", "full_name": "Mike Adams"},
            "Mike",
            id="first_name is missing",
        ),
        pytest.param(
            {
                "first_name": "Johnny",
                "last_name": "Holy",
                "full_name": "John Holy",
            },
            "Johnny",
            id="first_name already exists",
        ),
    ],
)
def test_restore_first_name(user: dict, expected_first_name: str) -> None:
    users = [user]

    restore_names.restore_names(users)

    assert users[0]["first_name"] == expected_first_name


def test_restore_names_for_mixed_users() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]

    restore_names.restore_names(users)

    assert [user["first_name"] for user in users] == ["Jack", "Mike"]


def test_restore_names_returns_nothing() -> None:
    assert restore_names.restore_names([]) is None
