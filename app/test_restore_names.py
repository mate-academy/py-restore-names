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
    ]
    expected = [
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
    restore_names(users)
    assert users == expected

    users = [
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "full_name": "Alice Smith",
        },
        {
            "first_name": "Bob",
            "last_name": "Jones",
            "full_name": "Bob Jones",
        },
    ]
    expected = [
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "full_name": "Alice Smith",
        },
        {
            "first_name": "Bob",
            "last_name": "Jones",
            "full_name": "Bob Jones",
        },
    ]
    restore_names(users)
    assert users == expected
