def restore_names(users: list[dict]) -> None:
    """Restaura o first_name dos usuários a partir do full_name se estiver ausente ou None."""
    for user in users:
        if "first_name" not in user or user["first_name"] is None:
            user["first_name"] = user["full_name"].split()[0]
