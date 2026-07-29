import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user, expected_users",
    [
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
        ), (
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
def test_restore_names_return_correct_dict(
        user: dict,
        expected_users: dict
) -> None:
    restore_names([user])

    assert user == expected_users
