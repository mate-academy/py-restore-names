import pytest
from app.restore_names import restore_names
from typing import Dict, List, Any


@pytest.fixture(scope="function")
def user_template() -> Dict[str, List[Dict[str, Any]]]:
    """Фікстура з трьома наборами користувачів для тестів restore_names."""
    return {
        "already_set": [
            {
                "first_name": "Emma",
                "last_name": "Stone",
                "full_name": "Emma Stone",
            }
        ],
        "none_first": [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }
        ],
        "missing_first": [
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }
        ],
    }


def test_first_name_already_set(
    user_template: Dict[str, List[Dict[str, Any]]]
) -> None:
    """Тест, коли first_name вже встановлено — нічого не змінюється."""
    restore_names(user_template["already_set"])
    assert user_template["already_set"][0]["first_name"] == "Emma"


def test_first_name_none_first(
    user_template: Dict[str, List[Dict[str, Any]]]
) -> None:
    """Тест, коли first_name = None — відновлюється з full_name."""
    restore_names(user_template["none_first"])
    assert user_template["none_first"][0]["first_name"] == "Jack"


def test_first_name_missing(
    user_template: Dict[str, List[Dict[str, Any]]]
) -> None:
    """Тест, коли first_name відсутній — додається і заповнюється."""
    restore_names(user_template["missing_first"])
    assert user_template["missing_first"][0]["first_name"] == "Mike"
