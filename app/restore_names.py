from typing import List


def restore_names(users: List[dict]) -> None:
    for user in users:
        if "first_name" not in user:
            user["first_name"] = user["full_name"].split()[0]

    for user in users:
        if user.get("first_name") is None:
            user["first_name"] = user["full_name"].split()[0]

