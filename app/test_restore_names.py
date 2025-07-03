from app.restore_names import restore_names
import pytest


@pytest.mark.parametrize(
    "dict_users, expected",
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
    ]
)
def test_restore_names(
        dict_users: list[dict],
        expected: dict
) -> None:
    restore_names(dict_users)
    assert dict_users == expected
