import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, result",
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
            id="function must work when `first_name` is `None`",
        ),
        pytest.param(
            [
                {
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
            id="function must work when `first_name` is not exist",
        ),
    ],
)
def test_restore_names_function(users: list, result: list) -> None:
    restore_names(users)
    assert users == result
