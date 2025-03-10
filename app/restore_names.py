from typing import Dict, List, Optional


def restore_names(users: List[Dict[str, Optional[str]]]) -> None:
    """
    Восстанавливает первые имена пользователей, если они отсутствуют.
    """
    for user in users:
        if "first_name" not in user or user["first_name"] is None:
            user["first_name"] = user["full_name"].split()[0]
