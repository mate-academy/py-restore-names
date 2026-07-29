import pytest
from typing import List
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "list_before,list_after",
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
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ], [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ]
        )
    ],
    ids=[
        "value for the first_name should be added when first_name = None",
        "value for the first_name should be added "
        "when key 'first_name' is missing",
        "nothing should be added when first_name "
        "key is present with the correct value",
    ]
)
def test_function_with_different_values_of_first_name_key(
        list_before: List[dict],
        list_after: List[dict]
) -> None:
    user = list_before
    restore_names(user)
    assert user == list_after
