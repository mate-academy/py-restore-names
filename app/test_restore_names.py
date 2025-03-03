import pytest
from app.restore_names import restore_names


@pytest.fixture
def users_data() -> None:
    return [
        {"first_name": None,
         "last_name": "Holy",
         "full_name": "Jack Holy"},

        {"last_name": "Adams",
         "full_name": "Mike Adams"},

        {"first_name": "Ricky",
         "last_name": "Martin",
         "full_name": "Ricky Martin"},
    ]


def test_restore_names_with_none(users_data: list) -> None:
    restore_names(users_data)

    assert users_data[0]["first_name"] == "Jack"
    assert users_data[1]["first_name"] == "Mike"
    assert users_data[2]["first_name"] == "Ricky"
