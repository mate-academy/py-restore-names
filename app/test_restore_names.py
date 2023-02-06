import pytest
from unittest import mock
from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> list:
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


def test_restore_names_works_correctly(users_template: callable) -> None:
    restore_names(users_template)
    assert users_template == [
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


def test_restore_names_was_called(users_template: callable) -> None:
    mock_function = mock.MagicMock()
    mock_function(users_template)
    mock_function.assert_called_once()
