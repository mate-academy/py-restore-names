import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_dict, expected",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ]
        ),
        (
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                }
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                }
            ]
        ),
        (
            [
                {
                    "first_name": "Mia",
                    "last_name": "Rain",
                    "full_name": "Mia Rain"
                }
            ],
            [
                {
                    "first_name": "Mia",
                    "last_name": "Rain",
                    "full_name": "Mia Rain"
                }
            ]
        ),
    ]
)
def test_first_name_added_if_is_none_or_not_exist(
        users_dict: list[dict],
        expected: list[dict]
) -> None:
    restore_names(users_dict)
    assert users_dict == expected
