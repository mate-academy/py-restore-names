import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "list_users, restore_list_users", [
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
            ], [
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
def test_restore_names(
        list_users: list[dict[str, str]],
        restore_list_users: list[dict[str, str]]
) -> None:
    restore_names(list_users)
    assert list_users == restore_list_users
