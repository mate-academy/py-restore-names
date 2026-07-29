import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_dict, result",
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
                    "full_name": "Mike Adams"
                },
                {
                    "first_name": "Jason",
                    "last_name": "Statham",
                    "full_name": "Jason Statham",
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                },
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                },
                {
                    "first_name": "Jason",
                    "last_name": "Statham",
                    "full_name": "Jason Statham",
                }
            ]
        )
    ],
    ids=[
        "testing everything"
    ]
)
def test_my_method(input_dict: list[dict], result: list[dict]) -> None:
    restore_names(input_dict)
    assert input_dict == result
