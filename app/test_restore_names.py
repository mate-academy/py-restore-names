import pytest
from app.restore_names import restore_names


@pytest.fixture
def incoming_data():
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


@pytest.fixture
def outcoming_data():
    return [
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
    ]


def test_restore_names(incoming_data, outcoming_data) -> None:
    assert incoming_data != outcoming_data
    restore_names(incoming_data)
    assert incoming_data == outcoming_data
