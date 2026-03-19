from typing import List, Dict, Any


def restore_names(users: List[Dict[str, Any]]) -> None:
    for user in users:
        missing_first = "first_name" not in user or user["first_name"] is None
        has_full = "full_name" in user

        if missing_first and has_full:
            user["first_name"] = user["full_name"].split()[0]
