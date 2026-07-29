from app.restore_names import restore_names


def test_adds_first_name_when_missing() -> None:
    user = {"full_name": "John Doe"}
    restore_names([user])
    assert user["first_name"] == "John"


def test_fixes_none_first_name() -> None:
    user = {"first_name": None, "full_name": "John Doe"}
    restore_names([user])
    assert user["first_name"] == "John"


def test_preserves_existing_first_name() -> None:
    user = {"first_name": "Bob", "full_name": "John Doe"}
    restore_names([user])
    assert user["first_name"] == "Bob"
