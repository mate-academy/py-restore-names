import pytest
from app.restore_names import restore_names


@pytest.fixture
def users_without_name() -> dict:
    users1 = [
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
    yield users1
    print("Test is finished")


def test_work_on_nameless_user(
        users_without_name: list
) -> AssertionError:
    users_true_name = [
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
    restore_names(users_without_name)
    assert (
        users_without_name == users_true_name
    ), f"Function should return {users_true_name}"


@pytest.fixture
def users_with_name() -> dict:
    users1 = [
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
    yield users1
    print("Test is finished")


def test_work_on_user_with_name(
        users_with_name: list) -> AssertionError:
    users_true_name = [
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
    restore_names(users_with_name)
    assert (
        users_with_name == users_true_name
    ), "Function should do nothing in such case"


@pytest.fixture
def users_mixed_name() -> dict:
    users1 = [
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
            "first_name": "Bruce",
            "last_name": "Wayne",
            "full_name": "Bruce Wayne",
        },
    ]
    yield users1
    print("Test is finished")


def test_work_on_user_with_mixed_name(
        users_mixed_name: list
) -> AssertionError:
    users_true_name = [
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
            "first_name": "Bruce",
            "last_name": "Wayne",
            "full_name": "Bruce Wayne",
        },
    ]
    restore_names(users_mixed_name)
    assert (
        users_mixed_name == users_true_name
    ), f"Function should return {users_true_name}"
