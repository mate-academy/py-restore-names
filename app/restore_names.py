from typing import List


def restore_names(users: List[dict]) -> None:
    for i, user in enumerate(users):
        if "first_name" not in user or user["first_name"] is None:
            full_name_parts = user["full_name"].split()
            user["first_name"] = full_name_parts[0]
            users[i] = {"first_name": full_name_parts[0], **user}
