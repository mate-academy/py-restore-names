import pytest
from app.restore_names import restore_names


@pytest.fixture
def sample_users() -> list:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_name_equal_to_real_name(sample_users: list) -> None:
    restore_names(sample_users)
    for user in sample_users:
        assert user["first_name"] == user["full_name"].split()[0]
