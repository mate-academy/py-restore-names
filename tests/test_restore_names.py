from app.restore_names import restore_names


def test_first_name_is_none():
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
            "first_name": None,
            "last_name": "Kristof",
            "full_name": "Sasha Adams",
        }
    ]

    restoring = restore_names(users)

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
            "first_name": "Sasha",
            "last_name": "Kristof",
            "full_name": "Sasha Adams",
        }
    ]

    assert restoring is None


def test_first_name_not_none():
    users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Kylie Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    restore_names(users)
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Kylie Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_empty_database():
    users = []
    restore_names(users)
    assert users == []
