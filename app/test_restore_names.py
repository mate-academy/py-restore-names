import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected",
    [
        (
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
            ]
        ),
        (
            [
                {
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
            ]
        )
    ]
)
def test_restore_correct_names(
        users: list[dict],
        expected: list[dict],
) -> None:
    restore_names(users)
    assert users == expected
