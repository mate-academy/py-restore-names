import pytest

from app.restore_names import restore_names


USERS = {
    "correct": [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ],
    "names_are_none": [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ],
    "names_are_absent": [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
}


@pytest.mark.parametrize(
    "users, expected",
    [
        pytest.param(
            USERS["names_are_none"],
            USERS["correct"],
            id="should restore names when `first_name` is set to None"
        ),
        pytest.param(
            USERS["names_are_absent"],
            USERS["correct"],
            id="should restore names when `first_name` is absent"
        )
    ]
)
def test_should_restore_names_set_to_none(users, expected):
    restore_names(users)
    assert users == expected
