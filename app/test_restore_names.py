import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected",
    [
        (
            [{
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }],
            ["Jack"]
        ),
        (
            [{
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
                {
                "first_name": None,
                "last_name": "Black",
                "full_name": "Bobby Black",
            }],
            ["Jack", "Bobby"]
        )
    ]
)
def test_correct_function_work(users, expected):
    restore_names(users)
    for i, names in enumerate(expected):
        assert users[i]["first_name"] == names
