from app.restore_names import restore_names

list_to_check = [
    {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
    {"last_name": "Adams", "full_name": "Mike Adams"},
]

result_list = [
    {"first_name": "Jack", "full_name": "Jack Holy", "last_name": "Holy"},
    {"first_name": "Mike", "full_name": "Mike Adams", "last_name": "Adams"},
]


def test_check_restore_users() -> None:
    restore_names(list_to_check)
    assert (
        list_to_check == result_list
    )
