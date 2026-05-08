from app.restore_names import restore_names


def test_restore_names_function() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Scale",
            "full_name": "Mike Scale"
        },
        {
            "last_name": "Bale",
            "full_name": "Luke Bale"
        },
        {
            "first_name": "Trix",
            "last_name": "Mark",
            "full_name": "Trix Mark"
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Scale",
            "full_name": "Mike Scale"
        },
        {
            "first_name": "Luke",
            "last_name": "Bale",
            "full_name": "Luke Bale"
        },
        {
            "first_name": "Trix",
            "last_name": "Mark",
            "full_name": "Trix Mark"
        }
    ]
