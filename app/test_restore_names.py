from app.restore_names import restore_names


def test_restore_names_with_none_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_restore_names_with_missing_first_name() -> None:
    users = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_restore_names_with_valid_first_name() -> None:
    users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_restore_names_with_only_one_name_in_full_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "",
            "full_name": "Cher",
        },
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "John",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Cher"
    assert users[1]["first_name"] == "John"


def test_restore_names_with_complex_full_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "John Michael Smith",
        },
        {
            "first_name": None,
            "last_name": "Doe",
            "full_name": "Jane Ann Doe",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Jane"


def test_restore_names_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_names_mixed_first_name_and_full_name() -> None:
    users = [
        {
            "first_name": "Alice",
            "last_name": "Johnson",
            "full_name": "Alice Johnson",
        },
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "Robert Smith",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Alice"
    assert users[1]["first_name"] == "Robert"
