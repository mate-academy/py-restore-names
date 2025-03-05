import pytest
from app.restore_names import restore_names


@pytest.fixture
def users_template() -> list:
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
        {
            "first_name": "Hello",
            "last_name": "World",
            "full_name": "Hello World",
        },
    ]


def test_should_restore_names(users_template: list) -> None:
    restore_names(users_template)
    assert users_template == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Hello",
            "last_name": "World",
            "full_name": "Hello World",
        },
    ]
