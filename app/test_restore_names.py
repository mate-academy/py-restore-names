import pytest
from app.restore_names import restore_names
import copy


@pytest.fixture
def users_data() -> list:
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


@pytest.fixture
def users(users_data: list) -> list:
    return copy.deepcopy(users_data)


def test_restore_first_name_for_user_who_first_name_is_equal_to_none(
    users: list,
) -> None:
    restore_names(users)
    with pytest.raises(AssertionError):
        assert users[0].get("first_name") != "Jack"


def test_restore_first_name_for_user_whithout_first_name(users: list) -> None:
    restore_names(users)
    with pytest.raises(AssertionError):
        assert users[1].get("first_name") != "Mike"
