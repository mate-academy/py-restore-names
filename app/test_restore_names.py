import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_output",
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
            id="test when key 'first_name' is  None"
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
            id="test when no key 'first_name'"
        )
    ]
)
def test_restore_names(
        users: list[dict], expected_output: list[dict]
) -> None:
    restore_names(users)
    assert users == expected_output
