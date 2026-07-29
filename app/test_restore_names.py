
from app.restore_names import restore_names


def test_restore_names_when_first_name_is_missing() -> None:
    users = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }

    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack", \
        "Should add 'first_name' if the key is missing"


def test_restore_names_when_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack", \
        "Should update 'first_name' if it is None"


def test_do_not_overwrite_existing_first_name() -> None:
    users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack", \
        "Should not overwrite an existing first_name"


def test_restore_names_for_multiple_users() -> None:
    users = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": None,
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_function_returns_none() -> None:
    users = [{"full_name": "Davy Jones", "last_name": "Jones"}]
    result = restore_names(users)
    assert result is None, \
        "The function should modify the list in-place and return None"
