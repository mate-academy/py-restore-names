from app.restore_names import restore_names
import pytest


@pytest.mark.parametrize(
    "user_dict, expected_dict", [
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
def test_check_first_name(
        user_dict: dict,
        expected_dict: dict
) -> None:
    restore_names([user_dict])
    assert user_dict == expected_dict



