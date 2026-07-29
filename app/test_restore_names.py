import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "test_dict, result",
    [
        (
            [{
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }],
            [{
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }]
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
        )
    ], ids=["firstname is None", "without firstname"]
)
def test_restore_names(test_dict: list[dict], result: list[dict]) -> None:
    restore_names(test_dict)
    assert test_dict == result
