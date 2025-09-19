from app.restore_names import restore_names


def test_restore_names() -> None:
    user = [{"full_name": "Alice Wonderland"}]
    restored = restore_names(user)
    assert restored == "Alice"
