from app.restore_names import restore_names


def test_check_only_missing_names() -> None:
    users = [
        {"full_name": "Karen Gillan"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Karen"


def test_check_only_none_names() -> None:
    users = [
        {"first_name": None, "full_name": "Jill Roberts"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jill"


def test_check_existing_name() -> None:
    users = [
        {"first_name": "Amy", "full_name": "Amy Pond"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Amy"
