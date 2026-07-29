import pytest
from app.restore_names import restore_names


@pytest.fixture()
def result_fix() -> list:
    return [{"first_name": "Jack",
             "last_name": "Holy",
             "full_name": "Jack Holy"}]


def test_name_equal_none(result_fix: callable) -> None:
    user = [{"first_name": None,
             "last_name": "Holy",
             "full_name": "Jack Holy"}]
    restore_names(user)
    assert user == result_fix


def test_name_empty(result_fix: callable) -> None:
    user = [{"last_name": "Holy", "full_name": "Jack Holy"}]
    restore_names(user)
    assert user == result_fix
