import pytest
from app.restore_names import restore_names


@pytest.fixture()
def first_user() -> bool:
    result = restore_names(
        [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }
        ]
    )
    return result == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


@pytest.fixture()
def second_user() -> bool:
    result = restore_names(
        [
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }
        ]
    )
    return result == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
