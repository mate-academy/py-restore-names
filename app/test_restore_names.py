import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "name,expected_value",
    [
        (
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy"
            },
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy"
            }
        ),
        (
            {
                "last_name": "Adams",
                "full_name": "Mike Adams"
            },
            {
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams"
            }
        )
    ]
)
def test_function_should_work_correctly(name: dict,
                                        expected_value: dict) -> None:
    restore_names([name])

    assert name == expected_value
