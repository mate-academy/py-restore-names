from typing import List, Dict, Any


def restore_names(users: List[Dict[str, Any]]) -> None:
    for user in users:
        if user.get("first_name") is None:
            full_name = user.get("full_name")
            if isinstance(full_name, str):
                parts = full_name.split()
                if parts:
                    user["first_name"] = parts[0]


def test_restore_names_handles_none_value() -> None:
    import app.restore_names as rn
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    rn.restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_handles_missing_key() -> None:
    import app.restore_names as rn
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    rn.restore_names(users)
    assert "first_name" in users[0]
    assert users[0]["first_name"] == "Mike"


def test_restore_names_modifies_in_place() -> None:
    import app.restore_names as rn
    user = {"full_name": "Alice Smith"}
    users = [user]
    rn.restore_names(users)
    assert users[0] is user
    assert user["first_name"] == "Alice"


def test_restore_names_no_overwrite() -> None:
    import app.restore_names as rn
    users = [{"first_name": "Jack", "full_name": "John Doe"}]
    rn.restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_empty_full_name() -> None:
    import app.restore_names as rn
    users = [{"full_name": ""}]
    rn.restore_names(users)
    assert "first_name" not in users[0]


def test_restore_names_whitespace_full_name() -> None:
    import app.restore_names as rn
    users = [{"full_name": "   "}]
    rn.restore_names(users)
    assert "first_name" not in users[0]


def test_restore_names_none_full_name() -> None:
    import app.restore_names as rn
    users = [{"full_name": None}]
    rn.restore_names(users)
    assert "first_name" not in users[0]


def test_restore_names_missing_full_name() -> None:
    import app.restore_names as rn
    users = [{"last_name": "Doe"}]
    rn.restore_names(users)
    assert "first_name" not in users[0]


def test_restore_names_invalid_type_full_name() -> None:
    import app.restore_names as rn
    users = [{"full_name": 123}]
    rn.restore_names(users)
    assert "first_name" not in users[0]
