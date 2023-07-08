from typing import Callable
import pytest
from app.restore_names import restore_names
from unittest import mock


@pytest.fixture
def test_func_data() -> None:
    yield [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }]


@pytest.fixture
def test_func_result() -> None:
    yield [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_func_is_was_called(test_func_data: Callable) -> None:
    with mock.patch("app.restore_names") as rest_name:
        rest_name(test_func_data)
        rest_name.assert_called_once_with(test_func_data)


def test_function_changes_state(
        test_func_data: Callable,
        test_func_result: Callable
) -> None:
    use_funk = restore_names(test_func_data)
    use_funk.assertEqual(test_func_data.state, test_func_result)
