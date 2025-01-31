import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_users, expected",
    [
        (
            [
                {
                    "first_name": "Jack",
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
            ],
        ),
        (
            [
                {
                    "first_name": None,
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
        ),
        (
            [
                {
                    "first_name": "",
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
        ),
        (
            [
                {
                    "first_name": "",
                    "last_name": "",
                    "full_name": "Mike Adams",
                }
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "",
                    "full_name": "Mike Adams",
                }
            ],
        ),
    ],
)
def test_restore_names(input_users: list[dict[str, str | None]], expected: list[dict[str, str]]) -> None:
    restore_names(input_users)
    assert input_users == expected
