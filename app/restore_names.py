from typing import List


def restore_names(users: List[dict]) -> None:
    for user in users:
        if "first_name" not in user or user.get("first_name") is None:
            full_name = user.get("full_name", "")
            if full_name.strip():  # Ensure full_name is not empty
                user["first_name"] = full_name.split()[0]
