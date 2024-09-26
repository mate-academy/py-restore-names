from app.restore_names import restore_names


def test_restore_first_name_absent() -> None:
    users = [
        {
            "last_name": "",
            "full_name": "Jack Holy"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_first_name_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_first_name_already_exists() -> None:
    users = [
        {
            "first_name": "Adam",
            "last_name": "Smith",
            "full_name": "Adam Smith"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Adam"


# def test_empty_full_name() -> None:
#     users = [
#         {
#             "first_name": None,
#             "last_name": "Smith",
#             "full_name": ""
#         }
#     ]
#     restore_names(users)
#     assert users[0]["first_name"] is None


def test_single_name_in_full_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Johnson",
            "full_name": "Emily"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Emily"
