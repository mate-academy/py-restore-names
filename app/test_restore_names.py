import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_before_changes, users_expected",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
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

                }
            ]
        )
    ]
)
def test_function_should_provide_correct_changes(
        users_before_changes: list[dict],
        users_expected: list[dict]
) -> None:
    restore_names(users_before_changes)
    assert users_before_changes == users_expected


def test_should_raise_correct_error() -> None:
    with pytest.raises(TypeError):
        restore_names(1)
