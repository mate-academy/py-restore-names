from app.restore_names import restore_names


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


def test_username_is_none() -> None:
    expected = "Jack"
    restore_names(users)
    actual = users[0]["first_name"]
    assert actual == expected


def test_first_name_is_empty() -> None:
    expected = "Mike"
    restore_names(users)
    actual = users[1]["first_name"]
    assert actual == expected
