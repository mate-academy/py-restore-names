import pytest
from app.restore_names import restore_names


@pytest.fixture
def user() -> list[dict]:
    return [
        {
            "first_name": None,
            "last_name": "Freecss",
            "full_name": "Gon Freecss",
        },
        {
            "last_name": "Zoldyck",
            "full_name": "Killua Zoldyck",
        },
    ]


def test_should_restore_missing_first_name(user: dict) -> None:
    restore_names(user)
    assert user == [
        {
            "first_name": "Gon",
            "last_name": "Freecss",
            "full_name": "Gon Freecss",
        },
        {
            "first_name": "Killua",
            "last_name": "Zoldyck",
            "full_name": "Killua Zoldyck",
        },
    ]
