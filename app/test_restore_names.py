from app.restore_names import restore_names


def test_restore_names_with_none_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_without_first_name_key() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_names_with_existing_first_name() -> None:
    users = [
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Anna Smith",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Anna"


def test_restore_names_mixed_cases() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "White",
            "full_name": "Tom White",
        },
        {
            "last_name": "Johnson",
            "full_name": "Sara Johnson",
        },
        {
            "first_name": "Emily",
            "last_name": "Clark",
            "full_name": "Emily Clark",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Tom"
    assert users[1]["first_name"] == "Sara"
    assert users[2]["first_name"] == "Emily"
