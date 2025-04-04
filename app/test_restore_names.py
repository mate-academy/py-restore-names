import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected", [
        (
            [{"first_name": None, "last_name": "Roberts", "full_name": "Julia Roberts"}],
            [{"first_name": "Julia", "last_name": "Roberts", "full_name": "Julia Roberts"}],
        ),
        (
            [{"last_name": "Walker", "full_name": "Paul Walker"}],
            [{"first_name": "Paul", "last_name": "Walker", "full_name": "Paul Walker"}],
        ),
        (
            [{"first_name": "Luke", "last_name": "Skywalker", "full_name": "Luke Skywalker"}],
            [{"first_name": "Luke", "last_name": "Skywalker", "full_name": "Luke Skywalker"}],
        )
    ]
)
def test_should_restore_names(users: list, expected: list) -> None:
    restore_names(users)
    assert users == expected
