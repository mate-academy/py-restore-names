from app.restore_names import restore_names


def test_if_first_name_is_available():
    users = [{
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy",
    },
        {
        "last_name": "Adams",
        "full_name": "Mike Adams",
    }
    ]
    restore_names(users)
    check2 = True
    for user in users:
        if "first_name" not in user or user["first_name"] is None:
            check2 = False
    assert check2 is True


def test_if_first_name_is_correct():
    users = [{
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy",
    },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
    }
    ]
    check2 = True
    restore_names(users)
    for user in users:
        if user["full_name"].split()[0] != user["first_name"]:
            check2 = False
    assert check2 is True
