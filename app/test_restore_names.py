import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "incoming_data,expected_result",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ]
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
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": "Johnson",
                    "full_name": "Anna Johnson",
                },
                {
                    "last_name": "Brown",
                    "full_name": "Emma Brown",
                }
            ],
            [
                {
                    "first_name": "Anna",
                    "last_name": "Johnson",
                    "full_name": "Anna Johnson",
                },
                {
                    "first_name": "Emma",
                    "last_name": "Brown",
                    "full_name": "Emma Brown",
                }
            ]
        ),
        (
            [
                {
                    "first_name": "Bob",
                    "last_name": "Smith",
                    "full_name": "Bob Smith",
                },
                {
                    "first_name": "George",
                    "last_name": "Clooney",
                    "full_name": "George Clooney",
                }
            ],
            [
                {
                    "first_name": "Bob",
                    "last_name": "Smith",
                    "full_name": "Bob Smith",
                },
                {
                    "first_name": "George",
                    "last_name": "Clooney",
                    "full_name": "George Clooney",
                }
            ]
        )
    ]
)
def test_should_return_dict_with_correct_first_name_key(
    incoming_data: list,
    expected_result: list
) -> None:
    restore_names(incoming_data)
    assert incoming_data == expected_result
