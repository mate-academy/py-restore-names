from app.restore_names import restore_names


def test_restore_names_updates_missing_and_none() -> None:
    users = [
        {"full_name": "John Doe"},
        {"first_name": None, "full_name": "Jane Smith"},
        {"first_name": "Alice", "full_name": "Alice Johnson"},
        {"full_name": "Madonna"}
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Jane"
    assert users[2]["first_name"] == "Alice"
    assert users[3]["first_name"] == "Madonna"


def test_empty_full_name_handling() -> None:
    users = [{"id": 4, "full_name": ""}]

    try:
        restore_names(users)
        assert users[0].get("first_name") is None
    except IndexError:
        pass


def test_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []
