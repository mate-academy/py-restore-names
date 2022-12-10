import pytest
from typing import List

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "list_to_restore,expected_restored_list",
    [
        pytest.param(
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
            id="None and not exsiting names should be replaced"
        )
    ]
)
def test_of_restore_name(
        list_to_restore: List[dict],
        expected_restored_list: List[dict]
) -> None:
    restore_names(list_to_restore)

    assert list_to_restore == expected_restored_list
