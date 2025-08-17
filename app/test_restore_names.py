import pytest
from app.restore_names import restore_names


@pytest.fixture()
def correct_users() -> list[dict]:
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


@pytest.fixture()
def incorrect_users() -> list[dict]:
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


def test_valid_users(correct_users: list[dict]) -> None:
    users = correct_users.copy()
    restore_names(users)
    assert users == correct_users


def test_invalid_users(incorrect_users: list[dict]) -> None:
    users = [user.copy() for user in incorrect_users]
    restore_names(users)
    assert users == [
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


@pytest.mark.parametrize(
    "users",
    [
        "hello",
        123,
        [1, 2, 3]
    ]
)
def test_invalid_type(users: list[dict]) -> None:
    with pytest.raises(TypeError):
        restore_names(users)


@pytest.mark.parametrize(
    "users",
    [
        [{
            "hel": 1,
            "sa": 2.3
        }]
    ]
)
def test_invalid_value(users: list[dict]) -> None:
    with pytest.raises(KeyError):
        restore_names(users)
