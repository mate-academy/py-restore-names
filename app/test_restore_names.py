import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected_users",
    [
        pytest.param([{"first_name": None, "full_name": "Jack Holy"}],
                     [{"first_name": "Jack", "full_name": "Jack Holy"}]),
        pytest.param([{"full_name": "Mike Adams"}],
                     [{"first_name": "Mike", "full_name": "Mike Adams"}])
    ]
)
def test_restore_names(users: list[dict], expected_users: list[dict]) -> None:
    restore_names(users)
    assert users == expected_users
