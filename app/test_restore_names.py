import pytest
from app.restore_names import restore_names


@pytest.fixture()
def name_is_none() -> dict:
    return {
        "first_name": None,
        "last_name": "Messi",
        "full_name": "Leo Messi",
    }


@pytest.fixture()
def key_name_is_absent() -> dict:
    return {"last_name": "Ronaldo", "full_name": "Cristiano Ronaldo"}


@pytest.fixture()
def list_to_test(name_is_none: dict, key_name_is_absent: dict) -> list:
    return [name_is_none, key_name_is_absent]


def test_names_restored_correctly(list_to_test: list) -> None:
    restore_names(list_to_test)
    assert list_to_test[1] == {
        "first_name": "Cristiano",
        "last_name": "Ronaldo",
        "full_name": "Cristiano Ronaldo",
    }

    assert list_to_test[0] == {
        "first_name": "Leo",
        "last_name": "Messi",
        "full_name": "Leo Messi",
    }
