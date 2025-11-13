from app.restore_names import restore_names


def test_restore_none_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": None,
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_restore_missing_first_name() -> None:
    users = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_preserve_existing_first_name() -> None:
    users = [
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Anna Smith"
        },
        {
            "first_name": "Leo",
            "last_name": "Brown",
            "full_name": "Leo Brown"
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Anna"
    assert users[1]["first_name"] == "Leo"


def test_mixed_cases() -> None:
    users = [
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Anna Smith"
        },
        {
            "first_name": None,
            "last_name": "Brown",
            "full_name": "Leo Brown"
        },
        {
            "last_name": "Stone",
            "full_name": "Mira Stone"
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Anna"
    assert users[1]["first_name"] == "Leo"
    assert users[2]["first_name"] == "Mira"
