import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user_before, user_after",
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
            ]
        ),
    ]
)
def test_restore_name(user_before: list[dict], user_after: list[dict]) -> None:
    assert restore_names(user_before) is None
    assert user_before == user_after
