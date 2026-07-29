from random import choice

import pytest

from app.restore_names import restore_names

first_name = "first_name"
last_name = "last_name"
full_name = "full_name"


@pytest.fixture()
def user_data() -> tuple:
    tests_names = ["Nick", "John", "Leslie"]
    users = []
    current_names = []
    missing_name = choice(tests_names)
    for name in tests_names:
        user = {
            first_name: None,
            last_name: "Adams",
            full_name: f"{name} Adams",
        }
        if name == missing_name:
            user.pop(first_name)
        users.append(user)
        current_names.append(name)
    return current_names, users


def test_missing_first_names_restored(user_data: tuple) -> None:
    users = user_data[1]
    restore_names(users)
    for user in users:
        assert first_name in user
        assert isinstance(user[first_name], str)


def test_restored_names_match_expected(user_data: tuple) -> None:
    expected_names, users = user_data
    restore_names(users)
    restored_names = [user[first_name] for user in users]
    assert expected_names == restored_names


def test_handles_non_dict_input() -> None:
    invalid_inputs = [None, "string", 123, ["list"]]
    for invalid_input in invalid_inputs:
        with pytest.raises(TypeError):
            restore_names(invalid_input)
