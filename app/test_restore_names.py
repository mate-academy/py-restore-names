import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> list[dict]:
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


def test_restore_names(users_template: list[dict]) -> None:
    restore_names(users_template)
    assert users_template[0]["first_name"] == "Jack"
    assert users_template[1]["first_name"] == "Mike"
