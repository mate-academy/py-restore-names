from app.restore_names import restore_names


def test_empty_value():
    user = [
        {
            "last_name": "Smith",
            "full_name": "Tim Smith",
        },
    ]

    result = [
        {
            "first_name": "Tim",
            "last_name": "Smith",
            "full_name": "Tim Smith",
        },
    ]

    restore_names(user)
    assert user == result


def test_none_value():
    user = [
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "Tim Smith",
        },
    ]

    result = [
        {
            "first_name": "Tim",
            "last_name": "Smith",
            "full_name": "Tim Smith",
        },
    ]

    restore_names(user)
    assert user == result
