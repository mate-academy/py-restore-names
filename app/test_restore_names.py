import pytest
from typing import List
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> List[dict]:
    yield [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]


def test_first_name_none(user_template: List[dict]) -> None:
    user = user_template
    user[0]["first_name"] = None
    restore_names(user)
    assert user[0]["first_name"] == "Jack"


def test_no_first_name(user_template: List[dict]) -> None:
    user = user_template
    del user[0]["first_name"]
    restore_names(user)
    assert user[0]["first_name"] == "Jack"


def test_first_name_is(user_template: List[dict]) -> None:
    user = user_template
    restore_names(user)
    assert user[0]["first_name"] == "Jack"
