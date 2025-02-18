from typing import List, Dict


def restore_names(users: List[Dict[str, str]]) -> None:
    for user in users:
        if ("first_name" not in user or user["first_name"]
                is None or user["first_name"] == ""):
            full_name = user.get("full_name", "").strip()
            if full_name:  # Ensure it's not empty after stripping spaces
                user["first_name"] = full_name.split()[0]
