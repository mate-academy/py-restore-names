import pytest
from app.restore_names import restore_names


@pytest.fixture()
def template_user() -> list[dict]:
    return [{"first_name": None,
             "last_name": "Holy",
             "full_name": "Jack Holy"},
            {"last_name": "Adams",
             "full_name": "Mike Adams"}]


def test_restore_names(template_user: list) -> None:
    restore_names(template_user)
    assert template_user[0]["first_name"] == "Jack"
    assert template_user[1]["first_name"] == "Mike"
