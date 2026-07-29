# flake8: noqa: *
import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",[
        pytest.param(
            [
                {
                    "first_name": "Mike",
                    "last_name": "Holy",
                    "full_name": "Mike Holy"
                }
            ], "Mike", id="Access option"
        ),
        pytest.param(
            [
                {
                    "last_name": "Holy",
                    "full_name": "Mike Holy"
                }
            ], "Mike", id="No first_name"
        ),
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Mike Holy"
                }
            ], "Mike", id="First name == None"
        )
    ]
)
def test_restore_names_logic(users, expected):
    restore_names(users)
    assert users[0].get("first_name") == expected


def test_restore_names_multiple_users():
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Anna Smith",
        },
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Anna",  # не изменилось
            "last_name": "Smith",
            "full_name": "Anna Smith",
        },
    ], "Multiple Users Error"
