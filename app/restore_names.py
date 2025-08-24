from typing import List


def restore_names(users: List[str]) -> List[str]:
    """
    Простая функция для примера:
    Принимает список строк и возвращает их с префиксом 'User: '.
    """
    return [f"User: {user}" for user in users]
