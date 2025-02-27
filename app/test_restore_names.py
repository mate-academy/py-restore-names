from app.restore_names import restore_names


def test_restore_names() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "full_name": "Alice Smith"
        },
        {
            "first_name": None,
            "last_name": "Brown",
            "full_name": "Charlie Brown"
        },
        {"last_name": "Williams", "full_name": "John"}
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Alice"
    assert users[3]["first_name"] == "Charlie"
    assert users[4]["first_name"] == "John"
