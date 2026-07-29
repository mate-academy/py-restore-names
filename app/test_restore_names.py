import pytest
from app.restore_names import restore_names


@pytest.fixture
def test_users() -> list[dict]:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
        {
            "first_name": "Mike",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]


@pytest.fixture
def expected_result() -> list[dict]:
    return [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
        {
            "first_name": "Mike",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]


def test_restore_names(
    test_users: list[dict],
    expected_result: list[dict]
) -> None:
    restore_names(test_users)
    assert test_users == expected_result
