from app.restore_names import restore_names


def test_is_firstname_correct():
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


def test_is_users_still_the_same_object():
    users = [
        {
            "first_name": None,
            "last_name": "Doe",
            "full_name": "John Doe",
        },
        {
            "last_name": "Vader",
            "full_name": "Dart Vader",
        },
        {
            "first_name": None,
            "last_name": "Baggins",
            "full_name": "Frodo Baggins",
        }
    ]
    id_before = id(users)
    restore_names(users)
    id_after = id(users)

    assert id_before == id_after


def test_are_other_keys_changed():
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

    assert users[0]["last_name"] == "Holy"
    assert users[1]["full_name"] == "Mike Adams"


def test_full_information():
    users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]
    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[0]["last_name"] == "Holy"
    assert users[0]["full_name"] == "Jack Holy"
