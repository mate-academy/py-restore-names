import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user_dict, expected", [
        (
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }, {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }
        ),
        (
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }, {
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }
        )
    ]
)
def test_restore_names(user_dict: dict, expected: dict) -> None:
    restore_names([user_dict])
    assert user_dict == expected
