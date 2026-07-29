import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "John Holy",
                }
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Holy",
                    "full_name": "John Holy",
                }
            ],
            id="user_with_none_first_name",
        ),
        pytest.param(
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
            ],
            id="user_without_first_name_key",
        ),
        pytest.param(
            [
                {
                    "first_name": "John",
                    "last_name": "Holy",
                    "full_name": "John Holy",
                }
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Holy",
                    "full_name": "John Holy",
                }
            ],
            id="user_with_first_name",
        ),
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "John Holy",
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Holy",
                    "full_name": "John Holy",
                },
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            id="two_users_simultaneously",
        ),
        pytest.param([], [], id="empty_list"),
    ],
)
def test_restore_names(users: list[dict], expected: list[dict]) -> None:
    restore_names(users)
    assert users == expected
