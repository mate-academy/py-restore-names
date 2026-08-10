from app import restore_names


def test_restore_names_handles_missing_and_none_fields() -> None:
    # 1. Готовим входные данные (матрица всех возможных вариантов)
    users = [
        # Случай 1: first_name равен None
        {"first_name": None, "last_name": "Holy", "full_name": "John Holy"},
        # Случай 2: Ключ first_name полностью отсутствует
        {"last_name": "Adams", "full_name": "Mike Adams"},
        # Случай 3: Имя уже заполнено правильно (не должно измениться)
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
    ]

    # 2. Вызываем тестируемую функцию
    restore_names.restore_names(users)

    # 3. Жестко проверяем ОЖИДАЕМЫЙ результат для каждого элемента
    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Jack"


def test_restore_names_leaves_other_fields_untouched() -> None:
    # Дополнительный тест: проверяем, что фамилии и полные имена не сломались
    users = [
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names.restore_names(users)

    assert users[0]["last_name"] == "Adams"
    assert users[0]["full_name"] == "Mike Adams"
