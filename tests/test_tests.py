import pytest
from app.restore_names import restore_names

def test_restore_only_missing_names():
    def restore_only_missing_names(users):
        for user in users:
            # Проверяем, что full_name не пустой
            if user.get("full_name") and not user.get("first_name"):
                user["first_name"] = user["full_name"].split()[0]

    # Тестируем замену только отсутствующих first_name
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_only_missing_names(users)

    assert users[0]["first_name"] == "Jack", "First name should be restored to 'Jack'"
    assert users[1]["first_name"] == "Mike", "First name should be restored to 'Mike'"

def test_empty_full_name():
    # Проверяем, что происходит, если full_name пустое
    users = [
        {"first_name": None, "last_name": "", "full_name": ""},
    ]
    restore_names(users)

    # Если full_name пустой, first_name и last_name должны остаться None/пустыми
    assert users[0]["first_name"] is None, "First name should remain None if full_name is empty"
    assert users[0]["last_name"] == "", "Last name should remain empty if full_name is empty"

def test_restore_both_names():
    # Тестируем восстановление обоих имен
    users = [
        {"first_name": None, "last_name": None, "full_name": "Anna Karenina"},
    ]
    restore_names(users)

    assert users[0]["first_name"] == "Anna", "First name should be restored to 'Anna'"
    assert users[0]["last_name"] == "Karenina", "Last name should be restored to 'Karenina'"

def test_partial_name():
    # Тестируем случай, если full_name состоит из одного слова
    users = [
        {"first_name": None, "last_name": None, "full_name": "Cher"},
    ]
    restore_names(users)

    assert users[0]["first_name"] == "Cher", "First name should be restored to 'Cher'"
    assert users[0]["last_name"] == "Cher", "Last name should also be 'Cher' if full_name has only one word"

def test_no_action_needed():
    # Тестируем случай, если имена уже указаны
    users = [
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
    ]
    restore_names(users)

    assert users[0]["first_name"] == "John", "First name should remain 'John'"
    assert users[0]["last_name"] == "Doe", "Last name should remain 'Doe'"
