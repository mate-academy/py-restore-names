from typing import List


def restore_names(users: List[dict]) -> None:
    for user in users:
        if "first_name" not in user or user["first_name"] is None:
            full_name_parts = user["full_name"].split()
            if full_name_parts:  # Sprawdza, czy lista nie jest pusta
                user["first_name"] = full_name_parts[0]
