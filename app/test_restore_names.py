import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "wrong_users, rule_users",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ]
        ),
        (
            [
                {
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ]
        ),
    ],
    ids=[
        "first_name is None",
        "first_name is not",
    ]
)
def test_restore_names(
        wrong_users: list[dict],
        rule_users: list[dict]) -> None:
    restore_names(wrong_users)
    assert wrong_users == rule_users
