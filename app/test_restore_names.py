from app import restore_names


def test_restore_names_with_none_first_name() -> None:
    users = [{"first_name": None, "full_name": "Jack Holy"}]
    expected = [{"first_name": "Jack", "full_name": "Jack Holy"}]
    restore_names.restore_names(users)
    assert users == expected


def test_restore_names_with_missing_first_name() -> None:
    users = [{"full_name": "Mike Adams"}]
    expected = [{"first_name": "Mike", "full_name": "Mike Adams"}]
    restore_names.restore_names(users)
    assert users == expected
