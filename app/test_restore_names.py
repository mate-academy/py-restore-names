from app.restore_names import restore_names


def test_restore_names_from_readme_example() -> None:
    # Arrange
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    expected_users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    # Act
    restore_names(users)

    # Assert
    assert users == expected_users


def test_restore_names_with_empty_list() -> None:
    # Arrange
    users = []

    # Act
    restore_names(users)

    # Assert
    assert users == []


def test_restore_names_does_not_change_correct_data() -> None:
    # Arrange
    users = [
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"}
    ]
    expected_users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]

    # Act
    restore_names(users)

    # Assert
    assert users == expected_users
