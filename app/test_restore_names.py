import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,correct_output",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ],
            id="first_name is equal to None",
        ),
        pytest.param(
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            id="first_name is missing",
        ),
    ],
)
def test_func(users: list[dict], correct_output: list[dict]) -> None:
    restore_names(users)
    assert users == correct_output
