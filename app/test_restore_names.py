import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list:
    yield [
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


def test_restore_names(user_template: list[dict]) -> None:
    assert restore_names(user_template) is None
    assert user_template == [
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
    ]
