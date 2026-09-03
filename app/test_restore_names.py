import app.restore_names as restore_names


def test_restores_first_name_when_none() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"}
    ]
    restore_names.restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restores_first_name_when_missing() -> None:
    users = [{"last_name": "Adams", "full_name": "Mike Adams"}]
    restore_names.restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_does_not_overwrite_existing_first_name() -> None:
    users = [
        {"first_name": "Anna", "last_name": "Lee", "full_name": "Anna Lee"}
    ]
    restore_names.restore_names(users)
    assert users[0]["first_name"] == "Anna"


def test_returns_none() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"}
    ]
    result = restore_names.restore_names(users)
    assert result is None
