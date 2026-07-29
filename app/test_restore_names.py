import app.restore_names as main


def test_restore_when_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]
    main.restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_when_first_name_is_missing() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]
    main.restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_does_not_overwrite_existing_first_name() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe"
        }
    ]
    main.restore_names(users)
    assert users[0]["first_name"] == "John"


def test_returns_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]
    assert main.restore_names(users) is None


def test_empty_list() -> None:
    users = []
    main.restore_names(users)
    assert users == []


def test_multiple_users() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe"
        }
    ]
    main.restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "John"
