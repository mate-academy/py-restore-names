import pytest
from app.restore_names import restore_names


@pytest.fixture()
def data_set_for_testing() -> list[dict]:
    data = [
        {
            "first_name": None,
            "last_name": "Owen",
            "full_name": "Clive Owen",
        },
        {
            "last_name": "Jones",
            "full_name": "Jon Jones",
        },
    ]
    return data


def test_restore_names_function(data_set_for_testing: list[dict]) -> None:
    restore_names(data_set_for_testing)
    assert data_set_for_testing == [
        {
            "first_name": "Clive",
            "last_name": "Owen",
            "full_name": "Clive Owen",
        },
        {
            "first_name": "Jon",
            "last_name": "Jones",
            "full_name": "Jon Jones",
        },
    ]
