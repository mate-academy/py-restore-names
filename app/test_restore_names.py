from app.restore_names import restore_names


def test_restore_first_name_when_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"


def test_restore_name_when_not_first_name() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]

    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_name_when_first_name_is_correct() -> None:
    users = [
        {
            "first_name": "Sarah",
            "last_name": "Brown",
            "full_name": "Sarah Brown"
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Sarah"
