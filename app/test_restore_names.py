from unittest import mock

import pytest
from app.restore_names import restore_names


@pytest.fixture(scope="function")
def user_template() -> None:
    users = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": None,
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    yield users


def test_should_return_jack(user_template: list) -> None:
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Jack"


def test_should_return_mike(user_template: list) -> None:
    restore_names(user_template)
    assert user_template[1]["first_name"] == "Mike"


def test_function_was_called(user_template: list) -> None:
    restore_names = mock.MagicMock()
    restore_names(user_template)
    restore_names.assert_called_once_with(user_template)


def test_should_return_none(user_template: list) -> None:
    assert restore_names(user_template) is None


def test_should_raise_error_if_users_is_str() -> None:
    with pytest.raises(TypeError):
        restore_names("user")
