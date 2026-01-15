import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user_dict, expected_dict",
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
                },
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ]

        ),
    ],
    ids=[
        "get_value_with_none_first_name_expected_first_name",
        "get_value_without_none_first_name",
    ]
)
def test_restore_names(
        user_dict: list[dict],
        expected_dict: list[dict]
) -> None:
    restore_names(user_dict)
    assert user_dict == expected_dict
