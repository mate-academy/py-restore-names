import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_ls, corrected_data",
    [
        pytest.param(
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
                },
            ],
            id="test restore missing names and None names"
        )
    ]
)
def test_check_if_first_name_will_be_corrected(users_ls, corrected_data):
    restore_names(users_ls)
    assert users_ls == corrected_data
