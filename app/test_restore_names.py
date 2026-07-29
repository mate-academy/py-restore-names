import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "list_name, expected",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            [
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
            ],
        )
    ],
)
def test_restore_names(list_name: list[dict], expected: list[dict]) -> None:
    """Тестирует функцию restore_names на корректное восстановление имён."""
    restore_names(list_name)
    assert list_name == expected
