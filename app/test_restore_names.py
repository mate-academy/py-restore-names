from app.restore_names import restore_names


def test_none_values_restored() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]
    restore_names(users)
    assert (
        users == [
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy"
            }
        ]
    )


def test_none_first_names_restored() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]
    restore_names(users)
    assert (
        users == [
            {
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams"
            }
        ]
    )
