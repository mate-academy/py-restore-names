import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "current_user_data, expected_user_data",
    [
        ([{
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }, {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        ], [{
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }, {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        ]),
    ]
)
def test_restore_names(current_user_data: list,
                       expected_user_data: list) -> None:
    # actual_user_data = restore_names(current_user_data)
    # assert actual_user_data == expected_user_data
    restore_names(current_user_data)
    assert expected_user_data == current_user_data
