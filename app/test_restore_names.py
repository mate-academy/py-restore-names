import pytest

from app.restore_names import restore_names


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
            id="first_name key is missing",
        ),
        pytest.param(
            {
                "first_name": "Johnny",
                "last_name": "Smith",
                "full_name": "John Smith",
            },
            "Johnny",
            id="existing first_name is not overwritten",
        ),
        pytest.param(
            {
                "first_name": "",
                "last_name": "Smith",
                "full_name": "John Smith",
            },
            "",
            id="empty first_name is not overwritten",
        ),
    ],
)
def test_restore_names_single_user(
    user: dict,
    expected_first_name: str,
) -> None:
    restore_names([user])

    assert user["first_name"] == expected_first_name


def test_restore_names_mixed_users() -> None:
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
            "first_name": "Anna",
            "last_name": "Lee",
            "full_name": "Anna Lee",
        },
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Anna",
            "last_name": "Lee",
            "full_name": "Anna Lee",
        },
    ]


def test_restore_names_returns_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]

    assert restore_names(users) is None


def test_restore_names_empty_list() -> None:
    users: list = []

    restore_names(users)

    assert users == []
