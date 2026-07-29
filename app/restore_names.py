from typing import List, Dict, Optional


def restore_names(users: List[Dict[str, Optional[str]]]) -> None:
    """
    Восстанавливает отсутствующие имена \
    пользователей на основе их полного имени.

    Args:
        users (list): Список словарей с \
        ключами 'first_name', 'last_name' и 'full_name'.
    """
    for user in users:
        if user.get("full_name"):
            if not user.get("first_name"):
                user["first_name"] = user["full_name"].split()[0]
            if not user.get("last_name"):
                user["last_name"] = user["full_name"].split()[-1]
