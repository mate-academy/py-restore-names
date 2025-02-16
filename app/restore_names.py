from typing import List


def restore_names(users: List[dict]) -> None:
    for user in users:
        if not user.get("first_name") and user.get("full_name"):
            name_parts = user["full_name"].split()
            if name_parts:  # Ensure full_name is not empty
                user["first_name"] = name_parts[0]
