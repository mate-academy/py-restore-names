from app.restore_names import restore_names


def test_restore_names_with_missing_first_name() -> None:
    users = [
        {
            "first_name": None, "last_name": "Holy", "full_name": "Jack Holy"
        },
        {"last_name": "Adams", "full_name": "Mike Adams"}
    ]
    restore_names(users)
    expected = [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]
    assert users == expected

def test_no_modification_for_valid_first_name() -> None:
    users = [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]
    restore_names(users)
    expected = [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]
    assert users == expected

def test_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []

def test_single_word_full_name() -> None:
    users = [
        {"first_name": None, "last_name": "", "full_name": "Sam"}
    ]
    restore_names(users)
    expected = [
        {"first_name": "Sam", "last_name": "", "full_name": "Sam"}
    ]
