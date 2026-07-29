import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_list, expected_list",
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
        )
    ]
)
def test_restore_names(
        users_list: list[dict],
        expected_list: list[dict]
) -> None:
    restore_names(users_list)
    assert users_list == expected_list
