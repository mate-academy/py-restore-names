from app.restore_names import restore_names


def test_restore_names_with_none() -> None:
    users = [{"first_name": None, "full_name": "Jack Holly"}]
    restore_names(users)
    assert users == [{"first_name": "Jack", "full_name": "Jack Holly"}]


def test_restore_names_with_no_first_name() -> None:
    users = [{"full_name": "Jack Holly"}]
    restore_names(users)


def test_restore_names_with_complete_first_name() -> None:
    users = [{"first_name": "Jack", "full_name": "Jack Holly"}]
    restore_names(users)
    assert users == [{"first_name": "Jack", "full_name": "Jack Holly"}]


def test_restore_names_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []
