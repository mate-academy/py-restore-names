def restore_names(users: list[dict]) -> None:
    for user in users:
        # só altera se não existir OU for None
        if user.get("first_name") is None:
            full_name = user.get("full_name")

            # garante que full_name existe e é válido
            if isinstance(full_name, str) and full_name.strip():
                first_name = full_name.strip().split()[0]
                user["first_name"] = first_name
