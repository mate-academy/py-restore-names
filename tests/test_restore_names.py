from app.restore_names import restore_names

def test_restore_names_basic():
    users = ["Alice", "Bob", "Charlie"]
    expected = ["User: Alice", "User: Bob", "User: Charlie"]
    assert restore_names(users) == expected

def test_restore_names_empty():
    assert restore_names([]) == []
