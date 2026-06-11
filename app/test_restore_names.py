import app.restore_names as restore_names


def test_first_name_is_empty() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Sparrow",
            "full_name": "Jack Sparrow"
        }
    ]
    restore_names.restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_user_without_first_name() -> None:
    users = [
        {
            "last_name": "Sparrow",
            "full_name": "Jack Sparrow"
        }
    ]
    restore_names.restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_user_with_first_name() -> None:
    users = [
        {
            "first_name": "Jack",
            "last_name": "Sparrow",
            "full_name": "Jack Sparrow"
        }
    ]
    restore_names.restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_a_few_users() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Sparrow",
            "full_name": "Jack Sparrow"
        },
        {
            "first_name": "Her",
            "last_name": "Brown",
            "full_name": "Her Brown"
        }
    ]
    restore_names.restore_names(users)
    assert users[0]["first_name"] == "Jack"
