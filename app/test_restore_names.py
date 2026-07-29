import pytest
from typing import List, Dict
from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> List[Dict[str, str | None]]:
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


def test_should_restore_names(
        users_template: List[Dict[str, str | None]]
) -> None:
    restore_names(users_template)
    assert users_template[0]["first_name"] == "Jack"
    assert users_template[1]["first_name"] == "Mike"
