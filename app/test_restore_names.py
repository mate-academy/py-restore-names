import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "list_to_fix,result",
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
            ]
        )
    ]
)
def test_restore_names(list_to_fix: list, result: list) -> None:
    restore_names(list_to_fix)
    assert list_to_fix == result
