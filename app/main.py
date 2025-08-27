from typing import List, Dict


def restore_names(users: List[Dict]) -> None:
    """
    Restaura o first_name dos usuários a partir do full_name caso esteja ausente
    ou seja None.
    """
    for user in users:
        # Se a chave não existir ou o valor for None, restaura a partir do full_name
        if user.get("first_name") is None:
            full_name = user.get("full_name", "")
            if full_name:
                user["first_name"] = full_name.split()[0]

# Linha em branco no final do arquivo
