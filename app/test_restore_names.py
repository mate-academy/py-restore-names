import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_inf() -> list:
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


def test_get_info(users_inf: list) -> None:
    restore_names(users_inf)
    assert users_inf[0]["first_name"] == "Jack"
    assert users_inf[1]["first_name"] == "Mike"
