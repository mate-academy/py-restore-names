from app.restore_names import restore_names


users_none_and_have_not = [
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


users_only_have_not_first_name = [
    {
        "last_name": "Holy",
        "full_name": "Jack Holy",
    },
    {
        "last_name": "Adams",
        "full_name": "Mike Adams",
    },
]


users_only_first_name_is_none = [
    {
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy",
    },
    {
        "first_name": None,
        "last_name": "Adams",
        "full_name": "Mike Adams",
    },
]


users_result = [
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


def test_users_name_is_none_and_have_not() -> None:
    restore_names(users_none_and_have_not)
    assert users_none_and_have_not == users_result


def test_users_name_only_with_have_not_name() -> None:
    restore_names(users_only_have_not_first_name)
    assert users_only_have_not_first_name == users_result


def test_users_name_only_first_name_is_none() -> None:
    restore_names(users_only_first_name_is_none)
    assert users_only_first_name_is_none == users_result
