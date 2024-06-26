from typing import List, Dict


def restore_names(users: List[Dict[str, str]]) -> None:
    for user in users:
        if (("first_name" not in user or user["first_name"] is None)
                and "full_name" in user):
            user["first_name"] = user["full_name"].split()[0]
