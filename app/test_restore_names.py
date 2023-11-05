import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, corrected_users",
    [(
        [{
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }, {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }],
        [{
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }, {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }]

    )]
)
def test_is_first_name_filled_correct(users: list[dict],
                                      corrected_users: list[dict]) -> None:
    restore_names(users)
    assert users == corrected_users
