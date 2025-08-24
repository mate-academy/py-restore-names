from typing import List, Dict, Optional


def restore_names(users: List[Dict[str, Optional[str]]]) -> None:
    """
    Restore missing or None first_name in each user dict
    using the full_name field.
    """
    for user in users:
        if (
            ("first_name" not in user or user["first_name"] is None)
            and "full_name" in user
            and user["full_name"]
        ):
            user["first_name"] = user["full_name"].split()[0]
