import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            id="test restore name value"
        )
    ]
)
def test_restore_name(users: list[dict], expected: list[dict]) -> None:
    restore_names(users)
    assert users == expected
