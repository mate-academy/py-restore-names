from typing import List, Dict


def restore_names(users: List[Dict]) -> None:
    for user in users:
        if user.get("first_name") is None:
            full_name = user.get("full_name", "")
            if full_name:
                user["first_name"] = full_name.split()[0]
