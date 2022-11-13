import pytest
from app.restore_names import restore_names
from typing import Any


@pytest.mark.parametrize(
    "user_input,user_expected",
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
        ),
    ],
)
def test_restore_first_name(user_input: Any, user_expected: Any) -> None:
    restore_names(user_input)
    assert user_input == user_expected
