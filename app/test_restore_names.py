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
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            id="test first_name is None",
        ),
        pytest.param(
            [{"last_name": "Adams", "full_name": "Mike Adams"}],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            id="test first_name key doesn't exist",
        ),
    ],
)
def test_restore_names(users: list, expected: list) -> bool:
    restore_names(users)
    assert users == expected
