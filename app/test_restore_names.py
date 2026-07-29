from app.restore_names import restore_names
from unittest import mock


def test_returns_nothing() -> None:
    with mock.patch("app.restore_names") as mocked_restore_names:
        mocked_restore_names()
        mocked_restore_names.assert_called_once_with()


def test_restores_only_if_no_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": "Anya",
            "last_name": "Bobson",
            "full_name": "Ame Bobson"
        },
        {
            "last_name": "Color",
            "full_name": "Cole Color"
        }
    ]
    restore_names(users)
    assert (
        users == [
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy"
            },
            {
                "first_name": "Anya",
                "last_name": "Bobson",
                "full_name": "Ame Bobson"
            },
            {
                "first_name": "Cole",
                "last_name": "Color",
                "full_name": "Cole Color"
            }
        ]
    )
