import pytest

from app.restore_names import restore_names


def test_restores_missing_first_name() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    result = restore_names(users)

    assert result is None
    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_restores_none_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]

    result = restore_names(users)

    assert result is None
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]


def test_preserves_existing_first_name() -> None:
    users = [
        {
            "first_name": "Preferred",
            "last_name": "Name",
            "full_name": "Full Name",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Preferred"


def test_restores_names_in_mixed_users_list() -> None:
    users = [
        {"first_name": None, "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {
            "first_name": "Existing",
            "full_name": "Another Person",
        },
    ]

    restore_names(users)

    assert [user["first_name"] for user in users] == [
        "Jack",
        "Mike",
        "Existing",
    ]


def test_accepts_empty_users_list() -> None:
    assert restore_names([]) is None


@pytest.mark.parametrize("full_name", ["Madonna", "  Mike   Adams  "])
def test_uses_first_nonempty_name_part(full_name: str) -> None:
    users = [{"full_name": full_name}]

    restore_names(users)

    assert users[0]["first_name"] == full_name.split()[0]
