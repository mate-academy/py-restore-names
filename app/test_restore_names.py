import pytest

from app.restore_names import restore_names


@pytest.fixture()
def users_with_missing_name() -> list:
    return [
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
            "last_name": "Adams",
            "full_name": "MikeAdams",
        },
        {
            "first_name": "qwe",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


users_formatted = [
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
        "first_name": "MikeAdams",
        "last_name": "Adams",
        "full_name": "MikeAdams",
    },
    {
        "first_name": "qwe",
        "last_name": "Adams",
        "full_name": "Mike Adams",
    }
]


def test_restore_names(users_with_missing_name: list) -> None:
    restore_names(users_with_missing_name)
    assert users_with_missing_name == users_formatted
