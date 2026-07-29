from app.restore_names import restore_names


def test_restore_names_when_first_name_is_missing() -> None:
    users = [
        {"last_name": "Adams",
         "full_name": "Mike Adams",
        }]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_names_when_first_name_is_none() -> None:
    users = [
        {"first_name": None,
         "second_name": "Smith",
         "full_name" : "John Smith",
        }]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_should_not_change_existing_first_name() -> None:
    users = [
        {"first_name" : "Russel",
         "second_name" : "Crawl",
         "full_name" : "Russel Crawl",
        }]
    restore_names(users)
    assert users[0]["first_name"] == "Russel"


def test_restore_names_for_multiple_users() -> None:
    users = [
        {"full_name": "John Doe"},
        {"first_name": None, "full_name": "Jane Doe"},
        {"first_name": "Bob", "full_name": "Robert Brown"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Jane"
    assert users[2]["first_name"] == "Bob"
