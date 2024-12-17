import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected_result",
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
                }
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
                }
            ]
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": None,
                    "full_name": "Marry Johnson",
                },
                {
                    "first_name": "Katrine",
                    "last_name": "Black",
                    "full_name": None,
                }
            ],
            [
                {
                    "first_name": "Marry",
                    "last_name": "Johnson",
                    "full_name": "Marry Johnson",
                },
                {
                    "first_name": "Katrine",
                    "last_name": "Black",
                    "full_name": "Katrine Black",
                }
            ]
        )
    ]
)
def test_restore_names(users: list[dict], expected_result: list[dict]) -> None:
    assert restore_names(users) == expected_result
