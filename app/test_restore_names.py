import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_users, expected_users",
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
            id="should produce the correct list as a result"
        )
    ]
)
def test_input_users(input_users: list, expected_users: list) -> None:
    restore_names(input_users)
    assert input_users == expected_users
