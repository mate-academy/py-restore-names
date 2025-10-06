from app.main import restore_names


def test_restore_names_with_none_and_missing_first_name() -> None:
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
    ]


def test_restore_names_does_not_change_valid_first_names() -> None:
    users = [
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Anna Smith",
        },
        {
            "first_name": "Leo",
            "last_name": "Brown",
            "full_name": "Leo Brown",
        },
    ]

    original = users.copy()
    restore_names(users)
    assert users == original


def test_restore_names_with_multiple_word_full_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Silva",
            "full_name": "Carlos Eduardo Silva",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Carlos"


def test_restore_names_with_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []
