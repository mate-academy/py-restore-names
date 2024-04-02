from app.restore_names import restore_names


def test_restore_names() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "", "last_name": "Smith", "full_name": " Smith"},
        {"first_name": "Alice",
         "last_name": "Wonderland", "full_name": "Alice Wonderland"}
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "John"
    assert users[2]["first_name"] == "Mike"
    assert users[3]["first_name"] == ""
    assert users[4]["first_name"] == "Alice"
