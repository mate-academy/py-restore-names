def restore_names(users: list[dict]) -> None:
    for user in users:
        if user.get("first_name") is None:
            full_name = user.get("full_name")

            if isinstance(full_name, str):
                name = full_name.strip()
                if name:
                    user["first_name"] = name.split()[0]
                else:
                    user["first_name"] = None
            else:
                user["first_name"] = None
