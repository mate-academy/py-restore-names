from app.restore_names import restore_names


def test_restore_name_function() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Gatiel",
            "full_name": "Andre Gariel"
        },
        {
            "last_name": "Haizenberg",
            "full_name": "Uolter Haizenberg"
        },
        {
            "first_name": "Robert",
            "last_name": "Ratler",
            "full_name": "Robert Ratler"
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Andre",
            "last_name": "Gatiel",
            "full_name": "Andre Gariel"
        },
        {
            "first_name": "Uolter",
            "last_name": "Haizenberg",
            "full_name": "Uolter Haizenberg"
        },
        {
            "first_name": "Robert",
            "last_name": "Ratler",
            "full_name": "Robert Ratler"
        }
    ]
