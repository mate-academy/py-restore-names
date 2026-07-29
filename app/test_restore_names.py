import pytest

from app.restore_names import restore_names


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


@pytest.mark.parametrize(
    "users,result",
    [
        (users, None)
    ],
    ids=[
        "users first name should be equal to None"
    ]
)
def test_restore_names(users: dict, result: None) -> None:
    restore_names(users)
    assert not users[0].get("first_name") == result
