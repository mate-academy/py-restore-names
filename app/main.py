from typing import List, Dict


def restore_names(users: List[Dict]) -> None:
    """
    Restaura o first_name dos usuários a partir do full_name caso esteja ausente
    ou seja None.
    """
    for user in users:
        # Caso a chave first_name não exista
        if "first_name" not in user:
            full_name = user.get("full_name", "")
            if full_name:
                user["first_name"] = full_name.split()[0]

        # Caso a chave first_name exista mas seja None
        elif user["first_name"] is None:
            full_name = user.get("full_name", "")
            if full_name:
                user["first_name"] = full_name.split()[0]
