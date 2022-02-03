from app.restore_names import restore_names
import copy


def test_function_nothing_to_return():
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

    assert restore_names(users) is None


def test_is_change_list():
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
    copy_users_dict = copy.deepcopy(users)
    restore_names(users)

    assert copy_users_dict is not users


def test_is_function_set_correct_first_name():
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
    restore_names(users)

    for data in users:
        assert data["first_name"] in data["full_name"]
