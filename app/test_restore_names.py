import pytest
from typing import List
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user,expected",
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
            id="should change first_name from None to Jack"
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
            id="should create first_name and set it like Jack"
        ),
    ]
)
def test_restore_names(user: List[dict], expected: List[dict]) -> None:
    restore_names(user)
    assert user == expected
