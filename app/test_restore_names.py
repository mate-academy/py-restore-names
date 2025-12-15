import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,result",
    [
        (
            [{
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy"
            }],
            [{
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy"
            }]
        ),
        (
            [{
                "last_name": "Adams",
                "full_name": "Mike Adams"
            }],
            [{
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams"
            }]
        )
    ],
    ids=[
        "test if first name none is restored",
        "test if no first name is restored"
    ]
)
def test_restore_names(users: list[dict], result: list[dict]) -> None:
    restore_names(users)
    assert users == result
