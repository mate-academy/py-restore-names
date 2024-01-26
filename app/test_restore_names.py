import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "broken_list,restored_list",
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
                {
                    "first_name": "Tom",
                    "last_name": "Dow",
                    "full_name": "Tom Dow",
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
                {
                    "first_name": "Tom",
                    "last_name": "Dow",
                    "full_name": "Tom Dow",
                },
            ]
        )
    ]
)
def test_restore_names(broken_list: list, restored_list: list) -> None:
    restore_names(broken_list)
    assert broken_list == restored_list
