def restore_names(users: list) -> None:
    for user in users:
        if not user.get("first_name"):
            user["first_name"] = user["full_name"].split()[0]
