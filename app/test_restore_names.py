from app.restore_names import restore_names


def test_should_check_restore_first_name_when_first_name_is_none():
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)

    assert users == [
        {"first_name": "Jack",
         "last_name": "Holy",
         "full_name": "Jack Holy",
         }
    ]


def test_should_check_restore_first_name_when_first_name_is_missing():
    users = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)

    assert users == [
        {"first_name": "Jack",
         "last_name": "Holy",
         "full_name": "Jack Holy",
         }
    ]
