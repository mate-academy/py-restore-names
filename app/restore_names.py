from typing import List, Dict, Any


def restore_names(users: List[Dict[str, Any]]) -> None:
    """Заполняет отсутствующие или None first_name из full_name."""
    for user in users:
        if "first_name" not in user or user["first_name"] is None:
            user["first_name"] = user["full_name"].split()[0]
