from .restore_names import restore_names


def test_restore_names() -> None:  # Добавлена аннотация возвращаемого типа
    # Тест 1: Пользователь с first_name равным None
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"

    # Тест 2: Пользователь с отсутствующим first_name
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"

    # Тест 3: Пользователь с уже заполненным first_name
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"

    # Тест 4: Пользователь с некорректным форматом full_name (только фамилия)
    users = [
        {
            "last_name": "Smith",
            "full_name": "Smith",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == ""  # Ожидается пустая строка

    # Тест 5: Пользователь с пустым full_name
    users = [
        {
            "last_name": "Johnson",
            "full_name": "",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == ""
