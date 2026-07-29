import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user_list, expected_first_name",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            "Jack",
        ),
        (
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            "Mike",
        ),
    ],
)
def test_restore_name(
        user_list: list,
        expected_first_name: str) -> None:
    restore_names(user_list)
    assert user_list[0]["first_name"] == expected_first_name
