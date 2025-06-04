import pytest
from typing import List
from app.restore_names import restore_names

# write your tests here

@pytest.mark.parametrize(
    "prediction, expected",
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
            [{
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }],
            [{
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }]
        ),
    ]
)
def test_restore_names(
        prediction: List[dict],
        expected: List[dict],
) -> None:
    restore_names(prediction)
    assert prediction == expected
