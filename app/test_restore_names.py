from app.restore_names import restore_names


def test_restore_names() -> None:
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

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_other_fields_unchanged() -> None:
    user = {
        "full_name": "Eve Smith",
        "last_name": "Smith",
        "age": 30
    }
    restore_names([user])

    assert user["last_name"] == "Smith"
    assert user["age"] == 30


def test_full_name_edge_cases() -> None:
    users = [
        {"full_name": "   Anne   Marie   Johnson  "},
        {"full_name": "Zendaya"},
        {"first_name": "", "full_name": "Test Name"}
    ]
    restore_names(users)

    assert users[0]["first_name"] == "Anne"
    assert users[1]["first_name"] == "Zendaya"
    assert users[2]["first_name"] == ""


def test_multiple_users() -> None:
    users = [
        {"first_name": None, "full_name": "A B"},
        {"full_name": "C D"},
        {"first_name": "E", "full_name": "E F"}
    ]
    restore_names(users)

    assert [u["first_name"] for u in users] == ["A", "C", "E"]
