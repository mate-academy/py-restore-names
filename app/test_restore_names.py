import pytest
from app.restore_names import restore_names
from unittest import mock


@pytest.mark.parametrize(
    "users, exp",
    [([
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ],
        [
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
    ])]
)
def test_restore_names_works(users: list, exp: list) -> None:
    restore_names(users)
    assert users == exp


def test_restore_names_returns() -> None:
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
    expected = None
    actual = restore_names(users)
    assert expected == actual


def test_restore_names_has_called() -> None:
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
    with mock.patch("app.restore_names.restore_names") as mock_restore:
        mock_restore(users)
        mock_restore.assert_called_once_with(users)
