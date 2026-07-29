import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_before, users_expected",
    [
        (
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
        ),
        (
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
        ),
        (
            [
                {
                    "first_name": "Jack",
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
        ),
    ]
)
def test_restore_names(users_before: list, users_expected: list) -> None:
    restore_names(users_before)
    assert users_before == users_expected
