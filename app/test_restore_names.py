import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_template():
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


def test_creates_first_name_key(users_template: list) -> None:
    restore_names(users_template)
    assert users_template[1]["first_name"]


def test_fills_first_name_from_full_name(users_template: list) -> None:
    restore_names(users_template)
    assert users_template[0]["first_name"] == "Jack"


def test_raises_type_error(users_template) -> None:
    with pytest.raises(TypeError):
        restore_names(1)
