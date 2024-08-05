import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
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
                },
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
                },
            ]
        ),
        (
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "first_name": "John",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "first_name": "John",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ]
        ),
    ],
    ids=[
        "if first_name is None or missing",
        "if the name exists or the full name does not contain this name"
    ]
)
def test_should_return_correct_result(users: list, expected: list) -> None:
    restore_names(users)

    assert users == expected


def test_should_always_return_none() -> None:
    assert restore_names([]) is None


def test_should_not_create_new_list_but_modify_the_given_one() -> None:
    given_list = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    copy = given_list

    restore_names(given_list)

    assert copy is given_list
