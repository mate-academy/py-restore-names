from typing import Dict, List, Optional


def restore_names(users: List[Dict[str, Optional[str]]]) -> None:
    """
    Восстанавливает первые имена пользователей, если они отсутствуют.
    """
    for user in users:
        # Проверяем, что поле first_name отсутствует или равно None
        if not user.get("first_name"):
            # Извлекаем первое имя из full_name
            full_name = user.get("full_name", "")
            first_name = full_name.split()[0]  # Разбиваем строку на части
            # Если имя пустое, ставим None, иначе присваиваем найденное имя
            user["first_name"] = (
                first_name if first_name else None
            )  # Применение условия на новой строке
