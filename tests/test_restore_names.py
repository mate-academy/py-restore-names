from app.restore_names import restore_names


def test_when_first_name_did_not_lose():
    users = [
        {
            "first_name": "Sheldon",
            "last_name": "Cooper",
            "full_name": "Sheldon Cooper",
        },
        {
            "first_name": "Leonard",
            "last_name": "Hofstadter",
            "full_name": "Leonard Hofstadter",
        }
    ]
    expected = [
        {
            "first_name": "Sheldon",
            "last_name": "Cooper",
            "full_name": "Sheldon Cooper",
        },
        {
            "first_name": "Leonard",
            "last_name": "Hofstadter",
            "full_name": "Leonard Hofstadter",
        }
    ]
    restore_names(users)
    assert users == expected


def test_when_first_name_is_none():
    users = [
        {
            "first_name": None,
            "last_name": "Wolowitz",
            "full_name": "Howard Wolowitz",
        },
        {
            "first_name": None,
            "last_name": "Hofstadter",
            "full_name": "Penny Hofstadter",
        }
    ]
    expected = [
        {
            "first_name": "Howard",
            "last_name": "Wolowitz",
            "full_name": "Howard Wolowitz",
        },
        {
            "first_name": "Penny",
            "last_name": "Hofstadter",
            "full_name": "Penny Hofstadter",
        }
    ]
    restore_names(users)
    assert users == expected


def test_when_first_name_lost():
    users = [
        {
            "last_name": "Geller",
            "full_name": "Monica Geller",
        },
        {
            "last_name": "Green",
            "full_name": "Rachel Green",
        }
    ]
    expected = [
        {
            "first_name": "Monica",
            "last_name": "Geller",
            "full_name": "Monica Geller",
        },
        {
            "first_name": "Rachel",
            "last_name": "Green",
            "full_name": "Rachel Green",
        }
    ]
    restore_names(users)
    assert users == expected
    # assert users is not expected
