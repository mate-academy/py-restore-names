import pytest
from app.restore_names import restore_names


@pytest.fixture
def sample_users() -> list:
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
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]


def test_restore_names_fills_missing_and_none_names(
    sample_users: list
) -> None:
    restore_names(sample_users)
    assert sample_users[0]["first_name"] == "Jack"
    assert sample_users[1]["first_name"] == "Mike"
    assert sample_users[2]["first_name"] == "John"


def test_restore_names_does_not_return_anything(sample_users: list) -> None:
    result = restore_names(sample_users)
    assert result is None


def test_restore_names_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_names_with_multiple_words_in_full_name() -> None:
    users = [{
        "last_name": "Van Houten",
        "full_name": "Milhouse Van Houten"
    }]
    restore_names(users)
    assert users[0]["first_name"] == "Milhouse"
