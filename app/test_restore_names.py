import pytest

from app.restore_names import restore_names


@pytest.fixture()
def none_or_not_exist_user() -> list[dict]:
    yield [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]


def test_restore_names(none_or_not_exist_user: list[dict]) -> None:
    restore_names(none_or_not_exist_user)
    assert none_or_not_exist_user == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]
