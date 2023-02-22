from app.restore_names import restore_names


def test_no_users() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_single_user_no_name() -> None:
    users = [
        {"full_name": "John Lock"}
    ]
    restore_names(users)
    assert users == [{"full_name": "John Lock", "first_name": "John"}]


def test_single_user_none_name() -> None:
    users = [
        {"full_name": "Bob Ross", "first_name": None}
    ]
    restore_names(users)
    assert users == [{"full_name": "Bob Ross", "first_name": "Bob"}]
