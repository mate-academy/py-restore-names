from copy import deepcopy

import pytest

from app.restore_names import restore_names


@pytest.fixture()
def mock_user() -> callable:

    def _user(
        full_name: str = "first_name last_name",
        is_first_name_key_present: bool = True,
        first_name_value: str = "first_name",
    ) -> dict:
        if is_first_name_key_present:
            return {
                "first_name": first_name_value,
                "full_name": full_name
            }
        return {"full_name": full_name}

    return _user


@pytest.fixture
def mock_user_list(mock_user: pytest.fixture) -> callable:

    def _user_list(how_many: int = 1, **kwargs) -> list[dict]:
        return [
            mock_user(**kwargs)
            for _ in range(how_many)
        ]

    return _user_list


def test_should_restore_first_name_when_first_name_is_none(
        mock_user_list: pytest.fixture
) -> None:
    users = mock_user_list(how_many=4, first_name_value=None)

    restore_names(users)

    for user in users:
        assert user.get("first_name") == "first_name", (
            "User's first_name key value should be restored if it was None"
        )


def test_should_restore_first_name_when_first_name_key_not_present(
        mock_user_list: pytest.fixture
) -> None:
    users = mock_user_list(how_many=4, is_first_name_key_present=False)

    restore_names(users)

    for user in users:
        assert user.get("first_name") == "first_name", (
            "User's first_name key should be restored "
            "if user had no first_name key"
        )


def test_should_do_nothing_when_first_name_present_and_not_none(
        mock_user_list: pytest.fixture
) -> None:
    users = mock_user_list(how_many=4)

    users_old = deepcopy(users)

    restore_names(users)

    assert users_old == users, (
        "Users shouldn't be modified if they have first_name key != None"
    )
