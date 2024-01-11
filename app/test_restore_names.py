import pytest
from app.restore_names import restore_names


@pytest.fixture
def users_with_missing_first_name() -> tuple:
    expected_result = [

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
    users = [
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
    yield users, expected_result


def test_restore_names_with_missing_first_name(
        users_with_missing_first_name: tuple
) -> None:
    users, expected_result = users_with_missing_first_name

    restore_names(users)
    assert users == expected_result


def test_restore_names_with_existing_first_name(
        users_with_missing_first_name: tuple
) -> None:
    users, expected_result = users_with_missing_first_name
    users[0]["first_name"] = "Jack"
    users[1]["first_name"] = ("Mike"
                              "")
    restore_names(users)

    assert users == expected_result
