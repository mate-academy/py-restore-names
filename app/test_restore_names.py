from app.restore_names import restore_names


def test_first_name_is_none() -> None:
    users = [{"first_name": None,
              "last_name": "Holy",
              "full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_first_name_missing() -> None:
    users = [{"last_name": "Adams", "full_name": "Mike Adams"}]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_first_name_already_set() -> None:
    users = [{"first_name": "Tom",
              "last_name": "Smith",
              "full_name": "Tom Smith"}]
    restore_names(users)
    assert users[0]["first_name"] == "Tom"


def test_mixed_users() -> None:
    users = [
        {"first_name": None,
         "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"last_name": "Adams",
         "full_name": "Mike Adams"},
        {"first_name": "Tom",
         "last_name": "Smith",
         "full_name": "Tom Smith"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Tom"


def test_returns_none() -> None:
    users = [{"first_name": None,
              "last_name": "Holy",
              "full_name": "Jack Holy"}]
    restore_names(users)
    result = restore_names(users)
    assert result is None


def test_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_full_name_multiple_parts() -> None:
    users = [{"first_name": None,
              "last_name": "Brown",
              "full_name": "Anna Marie Brown"}]
    restore_names(users)
    assert users[0]["first_name"] == "Anna"


def test_all_users_missing_first_name() -> None:
    users = [
        {"last_name": "Brown", "full_name": "Anna Brown"},
        {"last_name": "Lee", "full_name": "Bruce Lee"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Anna"
    assert users[1]["first_name"] == "Bruce"
