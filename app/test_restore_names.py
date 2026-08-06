import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "initial_user, expected_first_name",
    [
        # Case 1: first_name є None -> відновлюємо
        (
            {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
            "Jack",
        ),
        # Case 2: first_name відсутній -> відновлюємо
        (
            {"last_name": "Adams", "full_name": "Mike Adams"},
            "Mike",
        ),
        # Case 3: first_name вже є -> не змінюємо
        (
            {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
            "John",
        ),
        # Case 4: full_name складається з одного слова
        (
            {"first_name": None, "full_name": "Cher"},
            "Cher",
        ),
        # Case 5: full_name має зайві пробіли на початку чи між словами
        (
            {"first_name": None, "full_name": "   Alice   Smith  "},
            "Alice",
        ),
    ],
    ids=[
        "first_name_is_none",
        "first_name_missing",
        "first_name_exists",
        "single_word_full_name",
        "extra_spaces_in_full_name",
    ],
)
def test_restore_names_single_user(
    initial_user: dict, expected_first_name: str
) -> None:
    users = [initial_user]
    restore_names(users)
    assert users[0]["first_name"] == expected_first_name


def test_restores_mixed_users() -> None:
    users = [
        {"first_name": None, "full_name": "Jack Holy"},
        {"full_name": "Mike Adams"},
        {"first_name": "John", "full_name": "John Doe"},
    ]
    restore_names(users)
    assert [u["first_name"] for u in users] == ["Jack", "Mike", "John"]


def test_does_not_return_anything() -> None:
    users = [{"first_name": None, "full_name": "Jack Holy"}]
    assert restore_names(users) is None


def test_empty_list_does_not_raise_error() -> None:
    users = []
    restore_names(users)
    assert users == []
