import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_list, expected",
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
    ]
)
def test_restore_names(users_list: list, expected: list) -> None:
    restore_names(users_list)
    assert users_list == expected
