import pytest
from app.restore_names import restore_names
from typing import Any


@pytest.mark.parametrize(
    "user_input, expected_first_name",
    [
        ({"first_name": None, "full_name": "John Smith"}, "John"),
        ({"full_name": "Jane Doe"}, "Jane"),
        ({"full_name": "  Bob   Marley  "}, "Bob"),
        ({"full_name": "Madonna"}, "Madonna"),
    ]
)
def test_restore_first_name_when_missing(
        user_input: dict[str, Any], expected_first_name: str) -> None:
    restore_names([user_input])
    assert user_input["first_name"] == expected_first_name


@pytest.mark.parametrize(
    "user_input",
    [
        {"first_name": "Alice", "full_name": "Wrong Name"},
        {"first_name": "Taras", "full_name": "Taras Shevchenko"},
    ]
)
def test_do_not_overwrite_existing_first_name(
        user_input: dict[str, Any]) -> None:
    original = user_input.copy()
    restore_names([user_input])
    assert user_input == original


@pytest.mark.parametrize(
    "user_input",
    [
        {"full_name": ""},
        {},  # без full_name
        {"full_name": "   "},
    ]
)
def test_empty_or_missing_full_name(
        user_input: dict[str, Any]) -> None:
    restore_names([user_input])
    assert "first_name" not in user_input or not user_input["first_name"]


@pytest.mark.parametrize(
    "user_input",
    [
        {"full_name": 123},
        {"full_name": None},
        {"full_name": ["Ivan", "Petrov"]},
    ]
)
def test_non_string_full_name_raises_typeerror(
        user_input: dict[str, Any]) -> None:
    with pytest.raises(TypeError):
        restore_names([user_input])
