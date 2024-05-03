import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user,expected_name",
    [
        ([{
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }], "Jack"),
        ([{
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }], "Mike"),
        ([{
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }], "Jack")
    ],
    ids=[
        "If first name is 'None'",
        "If first name missing",
        "If first name is present"
    ]
)
def test_restore_name(user: list, expected_name: str) -> None:
    restore_names(users=user)
    assert user[0]["first_name"] == expected_name
