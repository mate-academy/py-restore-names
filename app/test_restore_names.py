from app.restore_names import restore_names


def test_restore_names_if_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holly"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_if_first_name_is_not() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_names_if_first_name_is_on() -> None:
    users = [
        {
            "first_name": "Emily",
            "second_name": "Watson",
            "full_name": "Emily Watson"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Emily"


def test_restore_names_if_all_three_examples_in_one() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holly"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
        {
            "first_name": "Emily",
            "second_name": "Watson",
            "full_name": "Emily Watson"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Emily"
