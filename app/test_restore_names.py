import pytest
from app.restore_names import restore_names


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
            ],
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": "Black",
                    "full_name": "Johnson Black",
                },
                {
                    "last_name": "Patty",
                    "full_name": "Luke Patty",
                },
            ],
            [
                {
                    "first_name": "Johnson",
                    "last_name": "Black",
                    "full_name": "Johnson Black",
                },
                {
                    "first_name": "Luke",
                    "last_name": "Patty",
                    "full_name": "Luke Patty",
                },
            ],
        ),
    ],
)
def test_restore_names(users: list[dict], expected: list[dict]) -> None:
    restore_names(users)
    assert users == expected


def test_restore_names_with_all_first_names_present() -> None:
    users = [
        {"first_name": "Anna", "last_name": "Smith",
         "full_name": "Anna Smith"},
        {"first_name": "Tom", "last_name": "Lee", "full_name": "Tom Lee"},
    ]
    expected = [
        {"first_name": "Anna", "last_name": "Smith",
         "full_name": "Anna Smith"},
        {"first_name": "Tom", "last_name": "Lee", "full_name": "Tom Lee"},
    ]
    restore_names(users)
    assert users == expected


def test_restore_names_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []
