import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_info, updated_users_info",
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
def test_restore_names_with_empty_first_name(users_info: list,
                                             updated_users_info: list) -> None:
    restore_names(users_info)
    assert users_info == updated_users_info
