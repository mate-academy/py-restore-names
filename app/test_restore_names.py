import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list[dict]:
    return [{
        "last_name": "Adams",
        "full_name": "Mike Adams",
    }]


def test_restore_names_without_firstname(
        user_template: list[dict]
) -> None:
    restore_names(user_template)

    assert user_template[0] == {
        "first_name": "Mike",
        "last_name": "Adams",
        "full_name": "Mike Adams"
    }


def test_restore_names_with_firstname_none(
        user_template: list[dict]
) -> None:
    user_template[0]["first_name"] = None
    restore_names(user_template)

    assert user_template[0] == {
        "first_name": "Mike",
        "last_name": "Adams",
        "full_name": "Mike Adams"
    }
