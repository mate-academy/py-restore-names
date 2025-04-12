from app.restore_names import restore_names


def test_restore_first_name_when_missing() -> None:
    users = [
        {"full_name": "John Doe", "first_name": None},
        {"full_name": "Jane Smith", "first_name": None}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Jane"


def test_restore_first_name_when_empty() -> None:
    users = [
        {"full_name": "John Doe"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_no_change_when_first_name_exists() -> None:
    users = [
        {"full_name": "John Doe", "first_name": "Johnny"},
        {"full_name": "Jane Smith", "first_name": "Janie"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Johnny"
    assert users[1]["first_name"] == "Janie"


def test_empty_user_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_first_name_from_full_name_without_first_name() -> None:
    users = [
        {"full_name": "John", "first_name": None},
        {"full_name": "Jane", "first_name": None}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Jane"


def test_split_first_name_and_last_name() -> None:
    users = [
        {"full_name": "John Doe", "first_name": None},
        {"full_name": "Jane Alice Smith", "first_name": None}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Jane"
