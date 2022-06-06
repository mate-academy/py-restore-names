import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            "Jack",
            id="first name is None"
        ),
        pytest.param(
            [
                {
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            "Jack",
            id="user don't have 'first_name'"
        )

    ]
)
def test_restore_names(users, expected):
    restore_names(users)
    assert users[0]["first_name"] == expected
