import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user_list, expected_result",
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
                    "full_name": "Mike Adams"
                },
            ],
            id="List: Jack Holy, Mike Adams",
        )
    ],
)
def test_restore_names(user_list: list, expected_result: list) -> None:
    restore_names(user_list)
    assert user_list == expected_result
