import pytest

from app import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        (
            [{"first_name": None, "last_name": "Holy",
              "full_name": "Jack Holy"}],
            [{"first_name": "Jack", "last_name": "Holy",
              "full_name": "Jack Holy"}],
        ),
        (
            [{"last_name": "Adams", "full_name": "Mike Adams"}],
            [{"first_name": "Mike", "last_name": "Adams",
              "full_name": "Mike Adams"}],
        ),
        (
            [{"first_name": "Ann", "last_name": "Lee",
              "full_name": "Ann Lee"}],
            [{"first_name": "Ann", "last_name": "Lee",
              "full_name": "Ann Lee"}],
        ),
        (
            [{"first_name": "Bob", "last_name": "Ray",
              "full_name": "Robert Ray"}],
            [{"first_name": "Bob", "last_name": "Ray",
              "full_name": "Robert Ray"}],
        ),
        (
            [],
            [],
        ),
    ],
)
def test_restore_names(users: list, expected: list) -> None:
    restore_names.restore_names(users)

    assert users == expected


def test_restore_names_returns_none() -> None:
    users = [{"last_name": "Adams", "full_name": "Mike Adams"}]

    assert restore_names.restore_names(users) is None
