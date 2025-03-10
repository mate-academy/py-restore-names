from typing import Dict, List, Optional


def restore_names(users: List[Dict[str, Optional[str]]]) -> None:
    """
    Восстанавливает первые имена пользователей, если они отсутствуют.
    """
    for user in users:
        if not user.get("first_name"):
            first_name = user.get("full_name", "").split()[0]
            user["first_name"] = first_name if first_name else None
