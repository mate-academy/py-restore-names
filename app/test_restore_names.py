import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Adams",
                    "full_name": "Jack Holy"
                }
            ],
            "Jack",
            id="should return 'Jack' if user is None"
        ),
        pytest.param(
            [
                {
                    "first_name": "Jack",
                    "last_name": "Adams",
                    "full_name": "Jack Holy"
                }
            ],
            "Jack",
            id="should do nothing if user is correct"
        ),
        pytest.param(
            [{"last_name": "Adams", "full_name": "Jack Holy"}], "Jack",
            id="should return 'Jack' if users is missing"
        )
    ]
)
def test_return_modify_users(users: list[dict], expected: str) -> None:
    restore_names(users)
    assert users[0]["first_name"] == expected
