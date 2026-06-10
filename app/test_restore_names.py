import app.restore_names


def test_restore_only_none_names() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    app.restore_names.restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_restore_only_missing_names() -> None:
    users = [
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
    ]
    app.restore_names.restore_names(users)
    assert users[0]["first_name"] == "Mike"
    assert users[1]["first_name"] == "Jack"


def test_does_not_overwrite_existing_first_name() -> None:
    users = [{"first_name": "John", "last_name": "Doe",
              "full_name": "Jack Doe"}]
    app.restore_names.restore_names(users)
    assert users[0]["first_name"] == "John"


def test_restore_names_returns_none() -> None:
    users = [{"first_name": None, "last_name": "Holy",
              "full_name": "Jack Holy"}]
    result = app.restore_names.restore_names(users)
    assert result is None


def test_restore_mixed_list() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "John", "last_name": "Doe", "full_name": "Jack Doe"},
    ]
    app.restore_names.restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "John"


def test_restore_empty_list() -> None:
    users = []
    app.restore_names.restore_names(users)
    assert users == []
