import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected_result",
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
            id="should work properly when first_name is None"
        ),
        pytest.param(
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            id="should work properly when no first_name key in dictionary"
        )
    ]
)
def test_restore_names(users: list[dict],
                       expected_result: list[dict]) -> None:
    restore_names(users)
    assert users == expected_result
