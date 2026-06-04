from typing import List
from app.restore_names import restore_names


def test_restore_names_when_first_name_is_none() -> None:
    """Vérifie la restauration lorsque 'first_name' vaut None."""
    # Arrange
    users: List[dict] = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    # Act
    restore_names(users)

    # Assert
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_restore_names_when_first_name_is_missing() -> None:
    """Vérifie la restauration lorsque la clé 'first_name' est absente."""
    # Arrange
    users: List[dict] = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    # Act
    restore_names(users)

    # Assert
    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_restore_names_should_not_overwrite_existing_first_name() -> None:
    """Vérifie qu'un 'first_name' déjà présent et valide n'est pas modifié."""
    # Arrange
    users: List[dict] = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "Johnny Doe",
        }
    ]

    # Act
    restore_names(users)

    assert users[0]["first_name"] == "John"


def test_restore_names_with_empty_list() -> None:
    # Arrange
    users: List[dict] = []

    # Act
    restore_names(users)

    # Assert
    assert users == []
