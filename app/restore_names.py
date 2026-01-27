from typing import List


def restore_names(users: List[dict]) -> None:
    for user in users:
        if user.get("first_name") is None:
            full_name = user.get("full_name", "")
            if full_name and full_name.strip():
                user["first_name"] = full_name.strip(
                ).split()[0]
