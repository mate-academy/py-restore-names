from typing import List


def restore_names(users: List[dict]) -> None:
    for user in users:
        if "first_name" not in user or user["first_name"] is None:
            user["first_name"] = user["full_name"].split()[0]
