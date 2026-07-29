from app.restore_names import restore_names


def test_restore_names() -> None:
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
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "full_name": "Alice Smith",
        },
        {
            "first_name": None,
            "last_name": "Doe",
            "full_name": "John Doe",
        },
    ]
    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Alice"
    assert users[3]["first_name"] == "John"


def test_empty_users() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_no_first_name_field() -> None:
    users = [
        {
            "first_name": "Charlie",
            "full_name": "Charlie Brown",
        },
    ]
    restore_names(users)

    assert users[0]["first_name"] == "Charlie"


def test_first_name_already_set() -> None:
    users = [
        {
            "first_name": "Eve",
            "last_name": "White",
            "full_name": "Eve White",
        },
    ]
    restore_names(users)

    assert users[0]["first_name"] == "Eve"


def test_full_name_with_multiple_spaces() -> None:
    users = [
        {
            "first_name": "None",
            "last_name": "Black",
            "full_name": "Bob black",
        }
    ]
    restore_names(users)

    assert users[0]["first_name"] == "None"
