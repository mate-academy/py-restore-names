from app import restore_names


def test_restore_only_none_names() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Black",
            "full_name": "Jack Black"
        },
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "John Smith"
        },
    ]
    restore_names.restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "John"


def test_restore_only_missing_names() -> None:
    users = [
        {
            "last_name": "Black",
            "full_name": "Jack Black"
        },
        {
            "last_name": "Smith",
            "full_name": "John Smith"
        },
    ]
    restore_names.restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "John"
