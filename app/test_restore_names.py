from app.restore import restore_names


def test_restore_missing_first_name() -> None:
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
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[0]["last_name"] == "Holy"
    assert users[1]["last_name"] == "Adams"


def test_restore_no_changes_if_first_name_present() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "full_name": "Alice Smith",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Alice"


def test_restore_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_first_name_empty_string() -> None:
    users = [
        {
            "first_name": "",
            "last_name": "Brown",
            "full_name": "Charlie Brown",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == ""


def test_restore_first_name_none_and_missing() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Taylor",
            "full_name": "Laura Taylor",
        },
        {
            "last_name": "Johnson",
            "full_name": "Emily Johnson",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Laura"
    assert users[1]["first_name"] == "Emily"
