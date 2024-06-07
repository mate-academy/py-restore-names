import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user_list, expected",
    [
        (
            [
                {"first_name": None,
                 "last_name": "Holy",
                 "full_name": "Jack Holy"},
                {"last_name": "Adams",
                 "full_name": "Mike Adams"},
            ],
            [
                {"first_name": "Jack",
                 "last_name": "Holy",
                 "full_name": "Jack Holy"},
                {"first_name": "Mike",
                 "last_name": "Adams",
                 "full_name": "Mike Adams"},
            ]
        ),
        (
            [
                {"first_name": None,
                 "last_name": "Smith",
                 "full_name": "John Smith"},
                {"first_name": "Jane",
                 "last_name": "Doe",
                 "full_name": "Jane Doe"},
            ],
            [
                {"first_name": "John",
                 "last_name": "Smith",
                 "full_name": "John Smith"},
                {"first_name": "Jane",
                 "last_name": "Doe",
                 "full_name": "Jane Doe"},
            ]
        ),
    ]
)
def test_restore_names(user_list: list, expected: list) -> None:
    restore_names(user_list)
    assert user_list == expected
