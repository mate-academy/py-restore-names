import copy

from app.restore_names import restore_names

users_expected = [
    {
        "first_name": "Mike",
        "last_name": "Adams",
        "full_name": "Mike Adams",
    }
]


def test_first_name_not_in_user() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert users == users_expected


def test_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert users == users_expected


def test_first_name_is_valid() -> None:
    users = [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert users == users_expected


def test_full_name_has_one_word() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike",
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike",
        }
    ]


def test_function_return_none() -> None:
    users_copy = copy.deepcopy(users_expected)
    assert restore_names(users_copy) is None
