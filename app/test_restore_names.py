import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected",
    [
        (
            [{
                "first_name": None,
                "last_name": "Doe",
                "full_name": "Jane Doe"
            }],
            [{
                "first_name": "Jane",
                "last_name": "Doe",
                "full_name": "Jane Doe"
            }]
        ),
        (
            [{
                "last_name": "Doe",
                "full_name": "Jane Doe"
            }],
            [{
                "first_name": "Jane",
                "last_name": "Doe",
                "full_name": "Jane Doe"
            }]
        ),
    ], ids=[
        "should restore name if it set like a None",
        "should restore name if first_name does not exist"
    ]
)
def test_should_correctly_restore_name(
        users: list[dict],
        expected: list[dict]
) -> None:
    restore_names(users)
    assert users == expected
