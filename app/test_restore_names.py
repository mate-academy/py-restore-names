import pytest
from app.restore_names import restore_names


@pytest.fixture
def users() -> list[dict[str, str | None] | dict[str, str]]:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_restore_names(users: list[dict]) -> None:
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


def test_restore_names_with_existing_first_name(users: list[dict]) -> None:
    users.append(
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    )

    restore_names(users)
    assert users[-1]["first_name"] == "John"


def test_restore_names_with_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []
