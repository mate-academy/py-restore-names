from app.restore_names import restore_names


def test_restore_names_when_first_name_is_none() -> None:
    # Caso 1: El campo existe pero es None
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_when_first_name_is_missing() -> None:
    # Caso 2: El campo ni siquiera existe en el diccionario
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_should_not_change_existing_first_name() -> None:
    # Caso 3: Si ya tiene un nombre válido, no debe sobreescribirse
    users = [
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "full_name": "Alice Smith",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Alice"


def test_restore_names_multiple_users() -> None:
    # Caso 4: Procesar múltiples usuarios simultáneamente
    users = [
        {"full_name": "John Doe"},
        {"first_name": None, "full_name": "Jane Smith"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Jane"
