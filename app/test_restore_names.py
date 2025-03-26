import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "current_value_of_dict_first_name, expected",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
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
                },
            ]
        ),
    ]
)
def test_restore_names(current_value_of_dict_first_name: list[dict],
                       expected: list[dict]) -> None:
    restore_names(current_value_of_dict_first_name)
    assert current_value_of_dict_first_name == expected
