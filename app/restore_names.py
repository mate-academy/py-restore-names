from typing import List, Dict


def restore_names(users: List[Dict[str, str]]) -> None:
    """
    Восстанавливает поле first_name для пользователей, у которых оно
    отсутствует или равно None. Восстановление происходит на основе
    поля full_name. Если full_name содержит только одно слово
    (фамилию), first_name остается пустым.
    """
    for user in users:
        if user.get("first_name") is None:
            full_name = user.get("full_name", "")
            # Разделяем full_name на части
            parts = full_name.split()
            # Если full_name содержит имя и фамилию (минимум два слова)
            if len(parts) >= 2:
                user["first_name"] = parts[0]  # Первое слово — имя
            else:
                user["first_name"] = ""
