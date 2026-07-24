import pytest

from app.restore_names import restore_names


def test_should_not_return_anything() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]
    assert restore_names(users) is None, (
        "Function should not return anything"
    )


def test_should_change_users_list_in_place() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack", (
        "Function should change the given list in place"
    )


def test_should_not_fail_on_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == [], (
        "Empty list should stay empty"
    )


@pytest.mark.parametrize(
    "users,expected",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ],
        ),
        (
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
        ),
        (
            [
                {
                    "first_name": "Bob",
                    "last_name": "Doe",
                    "full_name": "John Doe",
                },
            ],
            [
                {
                    "first_name": "Bob",
                    "last_name": "Doe",
                    "full_name": "John Doe",
                },
            ],
        ),
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
                {
                    "first_name": "Kate",
                    "last_name": "White",
                    "full_name": "Kate White",
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
                {
                    "first_name": "Kate",
                    "last_name": "White",
                    "full_name": "Kate White",
                },
            ],
        ),
    ],
    ids=[
        "should restore first name when it is none",
        "should restore first name when key is missing",
        "should not change existing first name",
        "should restore first names for several users",
    ],
)
def test_restore_names(users: list[dict], expected: list[dict]) -> None:
    restore_names(users)
    assert users == expected, (
        f"Users should be restored to {expected}"
    )
