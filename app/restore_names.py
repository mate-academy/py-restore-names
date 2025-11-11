from typing import List, Dict, Any


def restore_names(users: List[Dict[str, Any]]) -> None:
    for user in users:
        if not user.get("first_name"):
            full_name = user.get("full_name")
            if isinstance(full_name, str):
                parts = full_name.split()
                user["first_name"] = parts[0] if parts else ""
