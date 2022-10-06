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
            ], "Jack",
            id="first name should be Jack"
        ),
        pytest.param(
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ], "Mike",
            id="dict should have key: first_name and value Mike"
        ),
    ]
)
def test_correct_first_name(users: list, expected: str) -> None:
    restore_names(users)
    for user in users:
        assert user["first_name"] == expected
