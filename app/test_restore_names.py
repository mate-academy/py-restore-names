from app.restore_names import restore_names


def test_restore_names_missing_and_none() -> None:
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
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Anna Smith",
        },
    ]
    restore_names(users)
    assert users == [
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
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Anna Smith",
        },
    ]


def test_restore_names_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_names_multiple_words_full_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Johnson",
            "full_name": "Emily Jane Johnson",
        },
        {
            "last_name": "Brown",
            "full_name": "Chris Paul Brown",
        },
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Emily",
            "last_name": "Johnson",
            "full_name": "Emily Jane Johnson",
        },
        {
            "first_name": "Chris",
            "last_name": "Brown",
            "full_name": "Chris Paul Brown",
        },
    ]


def test_restore_names_first_name_present() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]
