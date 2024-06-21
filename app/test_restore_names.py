from typing import List, Dict, Optional

import pytest
from app.restore_names import restore_names


@pytest.fixture
def user_list() -> List[Dict[str, Optional[str]]]:
    return [
        {"full_name": "Jane Doe"},
        {"full_name": "Jack Holy", "first_name": None},
        {"full_name": "Mike Adams", "first_name": ""},
        {"full_name": "Mike Adams", "first_name": "Mike"}
    ]


def test_first_name_filled_where_missing(
        user_list: List[Dict[str, Optional[str]]]
) -> None:
    restore_names(user_list)
    assert user_list[0]["first_name"] == "Jane"
    assert user_list[1]["first_name"] == "Jack"
    assert user_list[2]["first_name"] == ""


def test_no_change_when_first_name_provided(
        user_list: List[Dict[str, Optional[str]]]
) -> None:
    restore_names(user_list)
    assert user_list[3]["first_name"] == "Mike"
