import pytest
from app.restore_names import restore_names

first = [
    {
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }
]
second = [
    {
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy",
    },
]
first_1 = [
    {
        "last_name": "Adams",
        "full_name": "Mike Adams",
    }
]
second_1 = [
    {
        "first_name": "Mike",
        "last_name": "Adams",
        "full_name": "Mike Adams",
    }
]


@pytest.mark.parametrize(
    "users_list, expected_list",
    [
        (first, second),
        (first_1, second_1),
    ],
)
def test_restore_names(users_list: list, expected_list: list) -> None:
    restore_names(users_list)
    assert users_list == expected_list
