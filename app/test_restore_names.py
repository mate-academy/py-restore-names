import pytest
from app.restore_names import restore_names


@pytest.fixture(scope="module")
def user_template() -> list:
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


def test_restore_names(user_template: list) -> None:
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Jack"
    assert user_template[0]["last_name"] == "Holy"
    assert user_template[0]["full_name"] == "Jack Holy"
    assert user_template[1]["first_name"] == "Mike"
    assert user_template[1]["last_name"] == "Adams"
    assert user_template[1]["full_name"] == "Mike Adams"
