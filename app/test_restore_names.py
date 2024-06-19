import pytest
from app.restore_names import restore_names

@pytest.mark.parametrize(
    "test_data, expected_result",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ]
        ),
        (
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ]
        ),
    ]
)
def test_restore_names(test_data: list[dict], expected_result: list[dict]):
    restore_names(test_data)
    assert test_data == expected_result
