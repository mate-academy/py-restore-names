import pytest
from app.restore_names import restore_names


@pytest.fixture()
def data_users() -> list:
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
        {
            "first_name": "Alex",
            "last_name": "Ivanov",
            "full_name": "Alex Ivanov",
        },
        {
            "first_name": "Maria",
            "last_name": "Petrova",
            "full_name": "Maria Petrova",
        },
    ]


def test_restore_names_if_absent_first_name(data_users: list) -> None:
    restore_names(data_users)
    assert data_users[0]["first_name"] == "Jack"
    assert data_users[1]["first_name"] == "Mike"


def test_restore_names_if_exist_first_name(data_users: list) -> None:
    restore_names(data_users)
    assert data_users[2]["first_name"] == "Alex"
    assert data_users[3]["first_name"] == "Maria"
