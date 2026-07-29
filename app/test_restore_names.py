from app.restore_names import restore_names


def test_restore_missing_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Doe",
            "full_name": "John Doe",
        },
        {
            "last_name": "Smith",
            "full_name": "Anna Smith",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Anna"


def test_first_name_already_present() -> None:
    users = [
        {
            "first_name": "Emily",
            "last_name": "Clark",
            "full_name": "Emily Clark",
        }
    ]
    original = users[0]["first_name"]
    restore_names(users)
    assert users[0]["first_name"] == original


def test_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_first_name_empty_string() -> None:
    users = [
        {
            "first_name": "",
            "last_name": "Brown",
            "full_name": "Charlie Brown",
        }
    ]
    restore_names(users)

    assert users[0]["first_name"] == ""
