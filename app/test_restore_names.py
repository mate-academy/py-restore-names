from app.restore_names import restore_names


def test_first_name() -> None:
    users = [

        {"first_name": None, "full_name": "Jack Holy"},

        {"full_name": "Mike Adams"},

        {"first_name": "Anna", "full_name": "Anna Smith"},

        {"first_name": "", "full_name": ""}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Anna"
    assert users[3]["first_name"] == ""
