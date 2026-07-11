import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("users", [
    [
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
            "first_name": "Alex",
            "last_name": "Smith",
            "full_name": "Alex Smith",
        }
    ]
])
def test_restore_names(users: list) -> None:
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
            "first_name": "Alex",
            "last_name": "Smith",
            "full_name": "Alex Smith",
        }
    ]


def test_restore_names_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []
