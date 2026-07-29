import app.restore_names


def test_restore_missing_first_name() -> None:
    users = [
        {"last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    app.restore_names.restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_restore_none_first_name() -> None:
    users = [
        {"first_name": None, "last_name": "Kent", "full_name": "Clark Kent"},
    ]
    app.restore_names.restore_names(users)
    assert users[0]["first_name"] == "Clark"


def test_preserve_existing_first_name() -> None:
    users = [
        {"first_name": "Lois", "last_name": "Lane", "full_name": "Lois Lane"},
    ]
    original = users[0]["first_name"]
    app.restore_names.restore_names(users)
    assert users[0]["first_name"] == original


def test_restore_with_only_one_name() -> None:
    users = [
        {"first_name": None, "last_name": None, "full_name": "Madonna"},
    ]
    app.restore_names.restore_names(users)
    assert users[0]["first_name"] == "Madonna"


def test_mixed_users_list() -> None:
    users = [
        {"first_name": None, "last_name": "Pitt", "full_name": "Brad Pitt"},
        {"first_name": "Tom",
         "last_name": "Cruise", "full_name": "Tom Cruise"},
        {"last_name": "Swift", "full_name": "Taylor Swift"},
    ]
    app.restore_names.restore_names(users)
    assert users[0]["first_name"] == "Brad"
    assert users[1]["first_name"] == "Tom"
    assert users[2]["first_name"] == "Taylor"
