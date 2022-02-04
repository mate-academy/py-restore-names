from app.restore_names import restore_names

def test_first_name_is_None_or_absent():
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": None,
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "last_name": "Masi",
            "full_name": "Michael Masi",
        }
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
            "first_name": "Michael",
            "last_name": "Masi",
            "full_name": "Michael Masi",
        }
    ]


def test_users_without_errors():
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
        {
            "first_name": "Michael",
            "last_name": "Masi",
            "full_name": "Michael Masi",
        }
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
            "first_name": "Michael",
            "last_name": "Masi",
            "full_name": "Michael Masi",
        }
    ]


def test_empty_list():
    users = []
    restore_names(users)
    assert users == []
