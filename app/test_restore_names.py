from app.restore_names import restore_names


def test_restore_only_none_names() -> None:
    users = [
        {"first_name": " ", "last_name": "Bo", "full_name": "Mike Bo"},
        {"first_name": " ", "last_name": "Bl", "full_name": "Anna Bl"}
    ]
    restore_names(users)
    assert users == [
        {"first_name": " ", "last_name": "Bo", "full_name": "Mike Bo"},
        {"first_name": " ", "last_name": "Bl", "full_name": "Anna Bl"}
    ]


def test_restore_missing_first_name_key() -> None:
    users = [
        {"last_name": "Sm", "full_name": "John Sm"},
        {"last_name": "Ta", "full_name": "Anna Ta"}
    ]
    restore_names(users)
    assert users == [
        {"first_name": "John", "last_name": "Sm", "full_name": "John Sm"},
        {"first_name": "Anna", "last_name": "Ta", "full_name": "Anna Ta"}
    ]


def test_restore_only_missing_names() -> None:
    users = [
        {"first_name": None, "last_name": "Sm", "full_name": "John Sm"},
        {"first_name": None, "last_name": "Ta", "full_name": "Anna Ta"}
    ]
    restore_names(users)
    assert users == [
        {"first_name": "John", "last_name": "Sm", "full_name": "John Sm"},
        {"first_name": "Anna", "last_name": "Ta", "full_name": "Anna Ta"}
    ]


def test_preserve_existing_first_name() -> None:
    users = [
        {"first_name": "Em", "last_name": "Bl", "full_name": "Em Bl"},
        {"first_name": "Ch", "last_name": "Ev", "full_name": "Ch Ev"}
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Em", "last_name": "Bl", "full_name": "Em Bl"},
        {"first_name": "Ch", "last_name": "Ev", "full_name": "Ch Ev"}
    ]


def test_empty_full_name() -> None:
    users = [
        {"first_name": None, "last_name": "Br", "full_name": "Jay Br"},
        {"first_name": None, "last_name": "Bl", "full_name": "Joe Bl"}
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jay", "last_name": "Br", "full_name": "Jay Br"},
        {"first_name": "Joe", "last_name": "Bl", "full_name": "Joe Bl"}
    ]


def test_empty_users_list() -> None:
    users = []
    restore_names(users)
    assert users == []
