from typing import List


def restore_names(users: List[dict]) -> None:
    for user in users:
        if user.get("first_name") is None or user["first_name"] == "":
            user["first_name"] = user["full_name"].split()[0]
