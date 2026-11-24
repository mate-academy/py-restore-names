import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("user, expected", [
    pytest.param(
        {"first_name": None, "full_name": "Jane Doe"},
        {"first_name": "Jane", "full_name": "Jane Doe"},
        id="First name is None",
    ),
    pytest.param(
        {"full_name": "Jane Doe"},
        {"first_name": "Jane", "full_name": "Jane Doe"},
        id="Full name is missing",
    )
])
def test_restore_names(user: dict[str, str | None],
                       expected: dict[str, str]) -> None:
    users = [user]
    restore_names(users)
    assert users == [expected]
