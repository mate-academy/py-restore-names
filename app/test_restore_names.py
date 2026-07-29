import pytest
from app.restore_names import restore_names


input_users = [
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

output_users = [
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
    ("input_users,output_users"),
    [
        pytest.param(input_users, output_users, id="standard_case"),
    ]
)
def test_restore_names(input_users: list, output_users: list) -> None:
    restore_names(input_users)
    assert input_users == output_users


if __name__ == "__main__":
    pass
