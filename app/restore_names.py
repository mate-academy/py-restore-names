from typing import List


def restore_names(users: List[dict]) -> None:
    for user in users:
        if "first_name" not in user or user["first_name"] is None:
            fn = user.get("full_name")

            if isinstance(fn, str):
                parts = fn.strip().split()

                if parts:
                    user["first_name"] = parts[0]
