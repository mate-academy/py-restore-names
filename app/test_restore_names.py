import pytest
from app.restore_names import restore_names


@pytest.fixture()
def template_user() -> list[dict]:
    return [{
        "last_name": "Adams",
        "full_name": "Mike Adams",
    }]


def test_should_restore_value(template_user: list) -> None:
    template_user[0]["first_name"] = None
    restore_names(template_user)
    assert template_user[0]["first_name"] == "Mike"


def test_should_restore_key_and_value(template_user: list) -> None:
    restore_names(template_user)
    assert "first_name" in template_user[0]
