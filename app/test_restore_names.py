import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, data",
    [
        pytest.param([
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
            [{
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
            id="test_existing_first_name")
    ]
)
def test_existing_first_name(users, data):
    restore_names(users)
    assert users == data
