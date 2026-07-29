import pytest

from unittest import mock

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_list, result_list",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ]
        ),
        (
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ]
        ),
        (
            [
                {
                    "first_name": "Lisa",
                    "last_name": "Black",
                    "full_name": "Lisa Black",
                }
            ],
            [
                {
                    "first_name": "Lisa",
                    "last_name": "Black",
                    "full_name": "Lisa Black",
                }
            ]
        )
    ]
)
@mock.patch("app.restore_names.restore_names")
def test_restore_names(
        mock_restore_names: mock.Mock,
        users_list: list,
        result_list: list
) -> None:
    mock_restore_names.return_value = users_list
    restore_names(users_list)
    assert users_list == result_list
