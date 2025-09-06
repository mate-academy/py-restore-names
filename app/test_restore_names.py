from app.restore_names import restore_names


def test_restore_when_first_name_is_none() -> None:
    users = [{"first_name": None, "last_name": "Holy",
              "full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_when_first_name_is_missing() -> None:
    users = [{"last_name": "Adams", "full_name": "Mike Adams"}]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_do_nothing_if_first_name_already_present() -> None:
    users = [{"first_name": "Jack", "last_name": "Holy",
              "full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_multiply_users() -> None:
    users = [
        {"first_name": None, "last_name": "Smith",
         "full_name": "Bob Smith"},
        {"last_name": "Brown", "full_name": "Mike Brown"},
        {"first_name": "Adam", "last_name": "McDonald",
         "full_name": "Adam McDonald"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Bob"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Adam"


def test_restore_when_full_name_has_one_word() -> None:
    users = [{"last_name": "",
              "full_name": "Gray"}]
    restore_names(users)
    assert users[0]["first_name"] == "Gray"
