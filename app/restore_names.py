from typing import List, Dict, Optional


def restore_names(users: List[Dict[str, Optional[str]]]) -> None:
    for user in users:
        if user.get("first_name") is None:
            full_name = user.get("full_name")
            if full_name:
                user["first_name"] = full_name.split()[0]
