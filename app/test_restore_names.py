import pytest

from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> list:
    return [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_restore_none_names(users_template: list) -> None:
    for user in users_template:
        user["first_name"] = None

    restore_names(users_template)

    for user in users_template:
        assert user["first_name"] == user["full_name"].split()[0]


def test_restore_missing_names(users_template: list) -> None:
    for user in users_template:
        del user["first_name"]

    restore_names(users_template)

    for user in users_template:
        assert user["first_name"] == user["full_name"].split()[0]
