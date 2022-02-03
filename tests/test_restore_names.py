from app.restore_names import restore_names


def test_always_none():
    assert restore_names([]) is None


def test_first_name_is_none_or_first_name_is_lost():
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
    assert users == users == [
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


def test_some_name_exists():
    users = [
        {
            "first_name": "Mike",
            "last_name": "Tramp",
            "full_name": "Mike Adams",
        },
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "James Smith",
        },
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Tramp",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "James",
            "last_name": "Smith",
            "full_name": "James Smith",
        },
    ]
