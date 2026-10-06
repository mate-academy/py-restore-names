import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user, expected",
    [
        ({"full_name": "Mike Adams"},
         {"full_name": "Mike Adams", "first_name": "Mike"}),
        ({"full_name": "Jack Holy", "first_name": None},
         {"full_name": "Jack Holy", "first_name": "Jack"}),
        ({"full_name": "Jack Holy", "first_name": "John"},
         {"full_name": "Jack Holy", "first_name": "John"}),
        ({"full_name": "Jack Holy", "first_name": ""},
         {"full_name": "Jack Holy", "first_name": ""}),
        ({"full_name": "Cher"},
         {"full_name": "Cher", "first_name": "Cher"}),
    ],
)
def test_restore_only_missing_or_none_names(
    user: dict, expected: dict
) -> None:
    users = [user]
    assert restore_names(users) is None
    assert users == [expected]
    assert users[0] is user


def test_empty_user_list() -> None:
    users = []
    assert restore_names(users) is None
    assert users == []


def test_restore_all_users_and_preserve_other_fields() -> None:
    users = [
        {"full_name": "Jack Holy", "first_name": None, "last_name": "Holy"},
        {"full_name": "Mike Adams", "last_name": "Adams"},
    ]
    restore_names(users)
    assert users == [
        {"full_name": "Jack Holy", "first_name": "Jack", "last_name": "Holy"},
        {"full_name": "Mike Adams", "first_name": "Mike",
         "last_name": "Adams"},
    ]
