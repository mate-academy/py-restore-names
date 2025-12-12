from app.restore_names import restore_names


def test_restore_first_name_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Doe",
            "full_name": "John Doe"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_restore_first_name_empty() -> None:
    users = [
        {
            "last_name": "Wazowski",
            "full_name": "Mike Wazowski"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_first_name_dont_change() -> None:
    users = [
        {
            "first_name": "James",
            "full_name": "James Sulivan"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "James"
