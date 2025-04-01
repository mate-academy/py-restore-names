import pytest
from app.restore_names import restore_names
from copy import deepcopy


@pytest.fixture(scope="function")
def get_users_list() -> list:
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


class TestRestoreNames:
    def test_restore_names_func(self, get_users_list: list) -> None:
        users = deepcopy(get_users_list)
        restore_names(users)

        if get_users_list[0]["first_name"] is None:
            assert users[0]["first_name"] == "Jack"

        if "first_name" not in get_users_list[1]:
            assert users[1]["first_name"] == "Mike"

    def test_restore_names_return_none(self, get_users_list: list) -> None:
        assert restore_names(get_users_list) is None
