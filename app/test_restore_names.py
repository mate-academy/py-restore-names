from app import restore_names


def test_restore_names_when_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names.restore_names(users)
    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_restore_names_when_first_name_is_missing() -> None:
    users = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names.restore_names(users)
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_restore_names_when_first_name_exists() -> None:
    users = [
        {
            "first_name": "Elza",
            "last_name": "Fon",
            "full_name": "Elza Fon",
        }
    ]
    restore_names.restore_names(users)
    assert users == [
        {
            "first_name": "Elza",
            "last_name": "Fon",
            "full_name": "Elza Fon",
        }
    ]
