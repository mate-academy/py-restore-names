import app.restore_names


def test_restore_names_when_first_name_is_none() -> None:
    users = [
        {"first_name": None, "last_name": "Holly", "full_name": "Jack Holy"}
    ]
    app.restore_names.restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_name_when_first_name_is_missing() -> None:
    users = [
        {"last_name": "Adams", "full_name": "Mike Adams"}
    ]
    app.restore_names.restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_names_should_not_change_existing_first_name() -> None:
    users = [
        {
            "first_name": "Anna",
            "last_name": "Kowalska",
            "full_name": "Anna Kowalska",
        }
    ]
    app.restore_names.restore_names(users)
    assert users[0]["first_name"] == "Anna"
