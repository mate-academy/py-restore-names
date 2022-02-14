from app.restore_names import restore_names
import pytest


@pytest.mark.parametrize(
    "lost_user_data,restored_user_data",
    [
        pytest.param(
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
            ],
            id="test restore None value"),
        pytest.param(
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
            ],
            id="test restore lost key")
    ]
)
def test_restore_names_with_lost_data(lost_user_data, restored_user_data):
    restore_names(lost_user_data)
    assert lost_user_data == restored_user_data


@pytest.mark.parametrize(
    "lost_user_data,restored_user_data",
    [
        pytest.param(
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            id="test with valid data")
    ]
)
def test_restore_names_with_valid_data(lost_user_data, restored_user_data):
    restore_names(lost_user_data)
    assert lost_user_data == restored_user_data
