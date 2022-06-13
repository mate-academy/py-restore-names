import pytest
from app.restore_names import restore_names

user_before = [
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

user_after = [
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
]


@pytest.mark.parametrize(
    "users,result",
    [
        (user_before, user_after),
    ],
)
def tests_get_coin_combination(users, result):
    restore_names(users)
    assert users == result, (
        f"Function should return {result}, when users are equal to {users}"
    )
