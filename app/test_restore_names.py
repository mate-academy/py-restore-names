from unittest import mock
import pytest

from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list[dict]:
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


def test_function_was_called() -> None:
    mock_f = mock.MagicMock()
    mock_f.restore_names(user_template)
    mock_f.restore_names.assert_called_once()


def test_restore_names(user_template: list[dict]) -> None:
    restore_names(user_template)
    assert user_template == [
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
