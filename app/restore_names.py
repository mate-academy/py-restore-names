from typing import List, Dict

def restore_names(users: List[Dict]) -> None:
    for user in users:
        if not user.get("first_name"):  # covers missing, None, or empty
            full_name = user.get("full_name", "")
            parts = full_name.strip().split()
            if parts:
                user["first_name"] = parts[0]
