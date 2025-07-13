from typing import List, Dict, Any

def restore_names(users: List[Dict[str, Any]]) -> None:
    for user in users:
        if "first_name" not in user or user["first_name"] is None:
            full_name = user.get("full_name")
            if full_name:
                user["first_name"] = full_name.split()[0]
