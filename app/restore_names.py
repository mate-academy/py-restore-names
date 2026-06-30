from typing import List


def restore_names(users: List[dict]) -> None:
    for user in users:
        for value in user.values():
            if (
                value is not None
                and not all(part.isalpha() for part in value.split())
            ):
                raise ValueError("Invalid data")
        if "full_name" not in user or user["full_name"] is None:
            raise KeyError("Full name is required")
        elif "first_name" not in user or not user["first_name"]:
            user["first_name"] = user["full_name"].split()[0]
