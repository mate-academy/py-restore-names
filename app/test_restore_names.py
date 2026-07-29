import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list[dict]:
    return [
        {
            "first_name": None,
            "last_name": "Jordan",
            "full_name": "Michael Jordan",
        },
        {
            "last_name": "Bryant",
            "full_name": "Kobe Bryant",
        },
    ]


def test_restore_names(user_template: list) -> None:
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Michael"
    assert user_template[1]["first_name"] == "Kobe"
