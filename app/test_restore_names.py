import pytest
from app.restore_names import restore_names


@pytest.fixture()
def results() -> list[dict]:
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
        },
    ]


@pytest.fixture()
def users() -> list[dict]:
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
    ]


def test_restoring_names_with_nones(
        users: list[dict],
        results: list[dict]
) -> None:
    users[0]["first_name"] = None
    restore_names(users)
    assert users == results


def test_restoring_deleted_names(
        users: list[dict],
        results: list[dict]
) -> None:
    del users[0]["first_name"]
    restore_names(users)
    assert users == results


def test_restoring_none_and_deleted_names(
        users: list[dict],
        results: list[dict]
) -> None:
    del users[0]["first_name"]
    users[1]["first_name"] = None
    restore_names(users)
    assert users == results
