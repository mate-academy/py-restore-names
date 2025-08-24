from app.restore_names import restore_names

def test_restore_names_basic():
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "Alice", "last_name": "Brown", "full_name": "Alice Brown"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "Alice", "last_name": "Brown", "full_name": "Alice Brown"},
    ]

def test_restore_names_empty_first_name():
    users = [
        {"first_name": "", "last_name": "Smith", "full_name": "John Smith"},
        {"first_name": None, "last_name": "Doe", "full_name": "Jane Doe"},
    ]
    restore_names(users)
    # В условии не сказано менять пустую строку, только None или отсутствие first_name
    # Поэтому пустая строка остаётся пустой строкой
    assert users == [
        {"first_name": "", "last_name": "Smith", "full_name": "John Smith"},
        {"first_name": "Jane", "last_name": "Doe", "full_name": "Jane Doe"},
    ]

def test_restore_names_no_full_name():
    users = [
        {"first_name": None, "last_name": "Unknown"},
        {"last_name": "Anonymous"},
    ]
    restore_names(users)
    # Если нет full_name, first_name не меняется (если нет - остаётся None или отсутствует)
    assert users == [
        {"first_name": None, "last_name": "Unknown"},
        {"last_name": "Anonymous"},
    ]

def test_restore_names_first_name_present():
    users = [
        {"first_name": "Emma", "last_name": "White", "full_name": "Emma White"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Emma", "last_name": "White", "full_name": "Emma White"},
    ]
