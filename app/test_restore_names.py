def test_restore_only_none_names() -> None:
    from app.restore_names import restore_names

    users = [
        {"first_name": None, "full_name": "Jack Holy"},
        {"first_name": None, "full_name": "Mike Adams"},
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_restore_only_missing_names() -> None:
    from app.restore_names import restore_names

    users = [
        {"full_name": "Jack Holy"},
        {"full_name": "Mike Adams"},
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_should_not_change_existing_names() -> None:
    from app.restore_names import restore_names

    users = [{"first_name": "Will", "full_name": "Will Turner"}]

    restore_names(users)

    assert users[0]["first_name"] == "Will"


def test_extra_spaces_and_return_none() -> None:
    from app.restore_names import restore_names

    users = [{"full_name": "  John   Doe  "}]

    assert restore_names(users) is None
    assert users[0]["first_name"] == "John"
