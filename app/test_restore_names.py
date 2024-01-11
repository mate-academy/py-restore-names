import pytest
from app.restore_names import restore_names


@pytest.fixture
def users_with_missing_first_name() -> list:
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


def test_restore_names_with_missing_first_name(
        users_with_missing_first_name: list
) -> None:
    users = users_with_missing_first_name
    restore_names(users)
    assert users == [
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


def test_restore_names_with_existing_first_name(
        users_with_missing_first_name: list
) -> None:
    users = users_with_missing_first_name
    users[0]["first_name"] = "Jack"
    users[1]["first_name"] = "Mike"
    restore_names(users)

    assert users == [

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
