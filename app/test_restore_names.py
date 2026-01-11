import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "failed_list, fixed_list",
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
def test_restore_names(failed_list: list, fixed_list: list) -> None:
    restore_names(failed_list)
    assert failed_list == fixed_list
